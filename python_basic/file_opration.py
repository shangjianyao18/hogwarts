# 文件操作

# 文件读取,w，编辑文件，如果文件存在，则直接覆盖，如果不存在，则直接创建
# file = open("data.txt",mode="w")
# 关闭文件，读取完毕之后顺手就关闭，省得占用内存，有些文件是打开后不手动关闭就不会关闭的，这种一定要手动关闭
# file.close()
# file.close()

# file1 = open("aa.py",mode="w")
# print(type(file1))
#
# ll = file1.write("print('hello')")
# print(f"共写入了{ll}个字符串")
# print(type(ll))
# file1.close()

# model = a ,已追加方式打开文件，光标在内容的最后，如没有则新创建
file2 = open("data.txt","a")
# file2.write("AAA")
# file2.write("VVVV")
# file2.write("wwww")

datas = ["AAAAAAAAAAAA\n","BBBBBBBBBBBB\n","CCCCCCCCCCCC\n","DDDDDDDDDDDD\n"]
file2.writelines(datas)
"""
先是打开文件，有多种方式，r是只读，w是写入，
已只都方式打开，后续的操作方法就是读取，可以读取整段，也可输入想要读取的字符的数量
已写入方式打开，后续就可以进行写入操作了
以只读方式打开，后续不能进行写入操作
以写入方式打开，后续不能进行读取操作
最后要记得关闭文件。
"""
#