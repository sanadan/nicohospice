#!/usr/bin/env ruby
# frozen_string_literal: true

#	ニコニコ動画巡礼教会
#	Ver. 1.0.1
#	by sanadan

require 'cgi'
require 'erb'

# 初期設定
DEFAULT_ID = 'sm0'
ITEMS = 10

# main
cgi = CGI.new
pos = cgi[ 'id' ].rindex( '/' )
id = ""
if pos != nil then
	# URIの場合
	id = cgi[ 'id' ].slice( pos + 1 .. -1 )
else
	id = cgi[ 'id' ].to_s
end
id = DEFAULT_ID if id == ""
print cgi.header  # ( { 'charset' => 'UTF-8' } )

head = id.slice( 0 .. 1 )
num = id.slice( 2 .. -1 ).to_i
prev_uri = ENV[ 'SCRIPT_NAME' ].to_s + '?id=' + head + ( num - ITEMS ).to_s
next_uri = ENV[ 'SCRIPT_NAME' ].to_s + '?id=' + head + ( num + ITEMS ).to_s

print ERB.new( IO.read( 'index.rhtml' ) ).result( binding )

