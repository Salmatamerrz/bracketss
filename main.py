def isbalanced(seq: str):
 stack = []
 opening = set('[({')
 close = set('])}')
 pair = {']': '[', ')': '(', '}': '{'}

 for i in seq:
   if i in opening:
     stack.append(i)
   if i in close:
       if not stack:
         return False

       elif pair[i] != stack.pop():
         return False

 return len(stack) == 0


if __name__ == '__main__':
 seq = '([{}]))'
 print('The sequence you entered is:',isbalanced(seq))
 print('due to unbalance')
 seq1 = '({]})'
 print('The sequence you entered is:', isbalanced(seq1))
 print('due to unequality')
 seq2 = '({[]})'
 print('The sequence you entered is:', isbalanced(seq2))
 print('congratulations its a perfect match')
 input('Thank you for trying out our program , do you like it?')



