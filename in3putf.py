#ファイル出力のサンプルプログラム

try:
    with open('insample.txt','r') as file_in:
        with open('outtext.txt','w') as file_out:
            i_all = file_in.read()
            o_all = file_out.write(i_all)

    print(o_all) 



except Exception as e:
    print(e.args)
