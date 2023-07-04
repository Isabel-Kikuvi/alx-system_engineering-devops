## 0x06. Regular expression

In this project, I have built regular expressions using Oniguruma, a regular expression library that which is used by Ruby by default. 
The Ruby code that is used is as follows, just replace the regexp part:

#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
