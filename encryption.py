#encryption code
# Jordan Adriano
# jan 9 2020
# This code will simply take a long string and swap each letter with their associated encryption in this large database

original= ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "!", "@", "#", "$", "%" "^", "&", "*", "-", "_", "+", "=", "~", "`", "{", "(", "[", "<", ">", "]", ")", "}", "\\", "/", "|", ":", ";" ,"?", ".", ",", "\""]

backwards= ["z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h", "g", "f", "e", "d", "c", "b", "a", "1", "2", "3", "4", "5", "6", "7", "8", "9", " "]

rot_01 = ["b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "!", "@", "#", "$", "%" "^", "&", "*", "-", "_", "+", "=", "~", "`", "{", "(", "[", "<", ">", "]", ")", "}", "\", "/", "|", ":", ";" ,"?", ".", ","]
rot_02 = ["c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "!", "@", "#", "$", "%" "^", "&", "*", "-", "_", "+", "=", "~", "`", "{", "(", "[", "<", ">", "]", ")", "}", "\", "/", "|", ":", ";" ,"?", ".", ","]
rot_03 = ["d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "!", "@", "#", "$", "%" "^", "&", "*", "-", "_", "+", "=", "~", "`", "{", "(", "[", "<", ">", "]", ")", "}", "\", "/", "|", ":", ";" ,"?", ".", ","]
rot_04 = ["e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "!", "@", "#", "$", "%" "^", "&", "*", "-", "_", "+", "=", "~", "`", "{", "(", "[", "<", ">", "]", ")", "}", "\", "/", "|", ":", ";" ,"?", ".", ","]
rot_09 = ["f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "!", "@", "#", "$", "%" "^", "&", "*", "-", "_", "+", "=", "~", "`", "{", "(", "[", "<", ">", "]", ")", "}", "\", "/", "|", ":", ";" ,"?", ".", ","]
rot_15 = ["p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", "!", "@", "#", "$", "%" "^", "&", "*", "-", "_", "+", "=", "~", "`", "{", "(", "[", "<", ">", "]", ")", "}", "\", "/", "|", ":", ";" ,"?", ".", ","]

twice     =["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii", "jj", "kk", "ll", "mm", "nn", "oo", "pp", "qq", "rr", "ss", "tt", "uu", "vv", "ww", "xx", "yy" "zz", "00", "11", "22", "33", "44", "55", "66", "77", "88", "99", "  ", "!!", "@@", "##", "$$", "%%" "^^", "&&", "**", "--", "__", "++", "==", "~~", "``", "{{", "((", "[[", "<<", ">>", "]]", "))", "}}", "\\", "//", "||", "::", ";;" ,"??", "..", ",,"]
triple    =["aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg", "hhh", "iii", "jjj", "kkk", "lll", "mmm", "nnn", "ooo", "ppp", "qqq", "rrr", "sss", "ttt", "uuu", "vvv", "www", "xxx", "yyy" "zzz", "000", "111", "222", "333", "444", "555", "666", "777", "888", "999", "   ", "!!!", "@@@", "###", "$$$", "%%%" "^^^", "&&&", "***", "---", "___", "+++", "===", "~~~", "```", "{{{", "(((", "[[[", "<<<", ">>>", "]]]", ")))", "}}}", "\\\", "///", "|||", ":::", ";;;" ,"???", "...", ",,,"]
quadruple =["aaaa", "bbbb", "cccc", "dddd", "eeee", "ffff", "gggg", "hhhh", "iiii", "jjjj", "kkkk", "lll", "mmm", "nnnn", "oooo", "pppp", "qqqq", "rrrr", "ssss", "tttt", "uuuu", "vvvv", "wwww", "xxxx", "yyyy" "zzzz", "0000", "1111", "2222", "3333", "4444", "5555", "6666", "7777", "8888", "9999", "    ", "!!!!", "@@@@", "####", "$$$$", "%%%%" "^^^^", "&&&&", "****", "----", "____", "++++", "====", "~~~~", "````", "{{{{", "((((", "[[[[", "<<<<", ">>>>", "]]]]", "))))", "}}}}", "\\\\", "////", "||||", "::::", ";;;;" ,"????", "....", ",,,,"]
quintuple =["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee", "fffff", "ggggg", "hhhhh", "iiiii", "jjjjj", "kkkkk", "llll", "mmmm", "nnnnn", "ooooo", "ppppp", "qqqqq", "rrrrr", "sssss", "ttttt", "uuuuu", "vvvvv", "wwwww", "xxxxx", "yyyyy" "zzzzz", "00000", "11111", "22222", "33333", "44444", "55555", "66666", "77777", "88888", "99999", "     ", "!!!!!", "@@@@@", "#####", "$$$$$", "%%%%%" "^^^^^", "&&&&&", "*****", "-----", "_____", "+++++", "=====", "~~~~~", "`````", "{{{{{", "(((((", "[[[[[", "<<<<<", ">>>>>", "]]]]]", ")))))", "}}}}}", "\\\\\", "/////", "|||||", ":::::", ";;;;;" ,"?????", ".....", ",,,,,"]
# etc for nth term with a for loop

for x in (range(11)):
    print(original[x])
