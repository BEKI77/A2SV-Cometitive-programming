import textwrap

def wrap(string, max_width):
    i=0;
    str='';
    while(i<len(string)): 
        str+= string[i:i+max_width]+'\n'
        i+=max_width
    return str

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
