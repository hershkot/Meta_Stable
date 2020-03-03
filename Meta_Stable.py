import numpy as np
from itertools import product
import math
####Written by Tomer Hershkovitz, for any questions reach me by mail tomerhz14@gmail.com######
##before using make sure you are using python3,you have numpy, you have itertools,you have math, if not use pip install

class Meta_Stable:
    def __init__(self,Function_path):
        """init function-
        input - Function_path a csv path of your reguler function (no MS values are allowed), insert in a gray order if not mention it in a flag below
        output - None
        F: {0,1}^n X {0,1}^n ---> {0,1}^m
        Example:
             import Meta_Stable
             M = Meta_Stable.Meta_Stable('/Users/tomerhershkovitz/Google_Drive/BGU_studies/Moti/Diamond_func.csv')
             """
        self.path = Function_path  ###Path to CSV of Boolean function
        self.func_list = self._read_Bool_func_from_csv_to_func_list()
        self.n = int(math.log2(self.func_list.__len__()))
        self.MS_Input = self.generate_MS_input(self.n)
        self.Input = self.generate_input(self.n)
        self.Insertion_Format = "Gray"  ##Gray/Binary order of your table





    def first_test(self):
        """This function is testing whether your Boolean MSc function is Associative according to test 1
         inputs - None
         outputs - Boolean
         Example:
             import Meta_Stable
             M = Meta_Stable.Meta_Stable('/Users/tomerhershkovitz/Google_Drive/BGU_studies/Moti/Diamond_func.csv')
             M.first_test()
         """
        for input_row in self.MS_Input:
            for input_col in self.MS_Input:
                inputs_concut = input_row + input_col
                Group_A = [self.func_list[self.list2ind(inputs, 'row')][self.list2ind(inputs, 'column')] for inputs in self.res(inputs_concut)]
                Group_B = self.res(self.star([self.func_list[self.list2ind(inputs, 'row')][self.list2ind(inputs, 'column')] for inputs in self.res(inputs_concut)]))
                for a in Group_A:
                    if [int(x) for x in a] not in Group_B:
                        print("1st condition not acheived here for row input {} and col input {} we receive f(res(x,y)) = {} & res(*f(res(x,y))) = {}".format(input_row,input_row,Group_A,Group_B))
                        return False
                for b in Group_B:
                    if [int(x) for x in b] not in Group_A:
                        print("1st condition not acheived here for row input {} and col input {} we receive f(res(x,y)) = {} & res(*f(res(x,y))) = {}".format(input_row,input_row,Group_A,Group_B))
                        return False
        print("you can use PPC your MS function is Associative, passed condition 1")
        return True


    def second_test(self):
        """This function is testing whether your Boolean MSc function is Associative according to test 2
         inputs - None
         outputs - Boolean
         Example:
             import Meta_Stable
             M = Meta_Stable.Meta_Stable('/Users/tomerhershkovitz/Google_Drive/BGU_studies/Moti/Diamond_func.csv')
             M.second_test()
         """
        for input_row in self.MS_Input:
            for input_col in self.MS_Input:
                inputs_concut = input_row + input_col
                A = [self.func_list[self.list2ind(inputs, 'row')][self.list2ind(inputs, 'column')] for inputs in self.res(inputs_concut)]
                B = self.res(self.star([self.func_list[self.list2ind(inputs, 'row')][self.list2ind(inputs, 'column')] for inputs in self.res(inputs_concut)]))
                for z in self.Input:
                    Group_A = [self.func_list[self.list2ind(input + z, 'row')][self.list2ind(input + z, 'column')] for input in A]
                    Group_B = [self.func_list[self.list2ind(input + z, 'row')][self.list2ind(input + z, 'column')] for input in B]
                    for a in Group_A:
                        if [int(x) for x in a] not in Group_B:
                            print("2nd condition not acheived here for row input {}, col input {} & z = {} we receive f(f(res(x,y)),z) = {} & f(res(*f(res(x,y))),z) = {}".format(input_row, input_row,z, Group_A, Group_B))
                            return False
                    for b in Group_B:
                        if [int(x) for x in b] not in Group_A:
                            print("2nd condition not acheived here for row input {}, col input {} & z = {} we receive f(f(res(x,y)),z) = {} & f(res(*f(res(x,y))),z) = {}".format(input_row, input_row, z, Group_A, Group_B))
                            return False
                    Group_A = [self.func_list[self.list2ind(z + input, 'row')][self.list2ind(z + input, 'column')] for input in A]
                    Group_B = [self.func_list[self.list2ind(z + input, 'row')][self.list2ind(z + input, 'column')] for input in B]
                    for a in Group_A:
                        if [int(x) for x in a] not in Group_B:
                            print("2nd condition not acheived here for row input {}, col input {} & z = {} we receive f(z,f(res(x,y))) = {} & f(z,res(*f(res(x,y)))) = {}".format(input_row, input_row,z, Group_A, Group_B))
                            return False
                    for b in Group_B:
                        if [int(x) for x in b] not in Group_A:
                            print("2nd condition not acheived here for row input {}, col input {} & z = {} we receive f(z,f(res(x,y))) = {} & f(z,res(*f(res(x,y)))) = {}".format(input_row, input_row, z, Group_A, Group_B))
                            return False
        print("you can use PPC your MS function is Associative, passed condition 2")
        return True


    def third_test(self):
        """This function is testing whether your Boolean MSc function is Associative according to test 3
         inputs - None
         outputs - Boolean
         Example:
             import Meta_Stable
             M = Meta_Stable.Meta_Stable('/Users/tomerhershkovitz/Google_Drive/BGU_studies/Moti/Diamond_func.csv')
             M.third_test()
         """
        for input_row in self.MS_Input:
            for input_col in self.MS_Input:
                inputs_concut = input_row + input_col
                A = [self.func_list[self.list2ind(inputs, 'row')][self.list2ind(inputs, 'column')] for inputs in self.res(inputs_concut)]
                B = self.res(self.star([self.func_list[self.list2ind(inputs, 'row')][self.list2ind(inputs, 'column')] for inputs in self.res(inputs_concut)]))
                for z in self.Input:
                    Group_A = [self.func_list[self.list2ind(input + z, 'row')][self.list2ind(input + z, 'column')] for input in A]
                    Group_B = [self.func_list[self.list2ind(input + z, 'row')][self.list2ind(input + z, 'column')] for input in B]
                    if self.star(Group_A) != self.star(Group_B):
                        print("3rd condition not acheived here for row input {}, col input {} & z = {} we receive *f(z,f(res(x,y))) = {} & *f(z,res(*f(res(x,y)))) = {}".format(input_row, input_row, z, self.star(Group_A), self.star(Group_B)))
                        return False
                    Group_A = [self.func_list[self.list2ind(z + input, 'row')][self.list2ind(z + input, 'column')] for input in A]
                    Group_B = [self.func_list[self.list2ind(z + input, 'row')][self.list2ind(z + input, 'column')] for input in B]
                    if self.star(Group_A) != self.star(Group_B):
                        print("3rd condition not acheived here for row input {}, col input {} & z = {} we receive *f(z,f(res(x,y))) = {} & *f(z,res(*f(res(x,y)))) = {}".format(input_row, input_row, z, self.star(Group_A), self.star(Group_B)))
                        return False
        print("you can use PPC your MS function is Associative, passed condition 3")
        return True

    def generate_input(self,bits_number):
        """This function create the boolean input stream according to n (number of bits in your inputs)
         inputs - bits number
         outputs - Boolean list of your inputs
         Example:
             import Meta_Stable
             M = Meta_Stable.Meta_Stable('/Users/tomerhershkovitz/Google_Drive/BGU_studies/Moti/Diamond_func.csv')
             M.generate_input(5)
         """
        return [list(x) for x in list(product([0, 1], repeat= bits_number))]

    def generate_MS_input(self, bits_number):
        """This function create the MS boolean input stream according to n (number of bits in your inputs)
         inputs - bits number
         outputs - Boolean list of your inputs
         Example:
             import Meta_Stable
             M = Meta_Stable.Meta_Stable('/Users/tomerhershkovitz/Google_Drive/BGU_studies/Moti/Diamond_func.csv')
             M.generate_MS_input(3)
         """
        return [list(x) for x in list(product([0, 1, 'M'], repeat = bits_number))]

    def _read_Bool_func_from_csv_to_func_list(self):
        """internal function: No Meta stable functions are allowed here, these are for functions from
        {0,1}^n X {0,1}^n --> {0,1}m, please insert the table in grey code order, if not state it at the flag in the init func"""
        func_list = []
        with open(self.path,'r') as M:
            for i,row in enumerate(M):
                if not i:
                    continue
                else:
                    temp = row.split(',')[1:]
                    func_list.append([[bool(int(cc)) for cc in x.split(' ')] for x in temp])
        return func_list

    def star(self,list_of_bool):
        """This function implements the MS star operator as defined in the lectures
         inputs - list of booleans from {0,1}^n
         outputs - the MS output of the operator
         Example:
             import Meta_Stable
             M = Meta_Stable.Meta_Stable('/Users/tomerhershkovitz/Google_Drive/BGU_studies/Moti/Diamond_func.csv')
             M.star([[0,0,1],[0,0,0],[False,True,False]])
             output: [False, 'M', 'M']
         """
        Sum_of_cols = [sum(x) for x in zip(*list_of_bool)]
        length = list_of_bool.__len__()
        Result = [True if v == length else False if v == 0 else 'M' for v in Sum_of_cols]
        return Result

    def dec_binary_list(self,dec_num,padding):
        return np.array([int(i) for i in list('{:0{}b}'.format(dec_num,padding))])

    def res(self,list_of_ms_inputs):
        """This function implements the res function as defined in the lectures
         inputs - an MS entry belongs to {0,1,'M'}^n
         outputs - a list of booleans that belongs to {0,1}^n
         Example:
             import Meta_Stable
             M = Meta_Stable.Meta_Stable('/Users/tomerhershkovitz/Google_Drive/BGU_studies/Moti/Diamond_func.csv')
             M.res([0,1,True,'M',False,'M'])
             output:
             [[False, True, True, False, False, False],
             [False, True, True, False, False, True],
             [False, True, True, True, False, False],
             [False, True, True, True, False, True]]
         """
        num_of_M = np.sum([1 for input in list_of_ms_inputs if input == 'M'])
        if not num_of_M:    return [list_of_ms_inputs]
        ind      = np.array([i for i,input in enumerate(list_of_ms_inputs) if input == 'M'])
        list_of_inputs = np.array([np.array([0 for j in range(list_of_ms_inputs.__len__())]) for i in range(2**num_of_M)])
        all_bin_opt = np.array([self.dec_binary_list(i,num_of_M) for i in range(2**num_of_M)])
        for i in range(2**num_of_M):
            temp = np.array(list_of_ms_inputs)
            temp[ind] = all_bin_opt[i]
            temp = [1 if (itr == '1' or itr == 'True') else 0 for itr in temp ]
            list_of_inputs[i] = temp
        return [[bool(a) for a in BOOL] for BOOL in list_of_inputs]   ###change here

        # return list_of_inputs  ###change here

    def list2ind(self,list_of_inputs,RowOrCol):
        length = list_of_inputs.__len__()
        if RowOrCol == 'row':
            Relevent_input = list_of_inputs[0:int(length / 2)]
        else:
            Relevent_input = list_of_inputs[int(length/2):]
        Relevent_input_bin = self.graytoBinary(Relevent_input)
        return np.sum([2 ** i * x for i, x in enumerate(Relevent_input_bin[::-1])])

    def F_closer(self,inputs):
        """This function implements the F closer by definition *f(res(x))) as defined in the lectures
         input - a MS input that belongs to {0,1,'M'}
         output - the value of the F_closer on that input
         Example:
             import Meta_Stable
             M = Meta_Stable.Meta_Stable('/Users/tomerhershkovitz/Google_Drive/BGU_studies/Moti/Diamond_func.csv')
             M.F_closer([0,1]+[True,'M'])
             output: [False, True]
         """
        return self.star([self.func_list[self.list2ind(inputs, 'row')][self.list2ind(inputs, 'column')] for inputs in self.res(inputs)])

    def Is_associative(self,inputs):
        """This function Tests by definition if your function is Associative or not
         inputs - can be boolean inputs or MS boolean inputs.
         outputs - Boolean
         Example:
             import Meta_Stable
             M = Meta_Stable.Meta_Stable('/Users/tomerhershkovitz/Google_Drive/BGU_studies/Moti/Diamond_func.csv')
             M.Is_associative(M.MS_Input)
             output: test ended good! your function is associative you can use PPC!!!
         """
        flag = 0
        for x in inputs:
            for y in inputs:
                for g in inputs:
                    temp1 = self.F_closer(x + y) + g
                    result1 = self.F_closer(temp1)
                    temp2 = x + self.F_closer(y + g)
                    result2 = self.F_closer(temp2)
                    if result1 != result2:
                        print(
                            "the function is not associative it failed on x = {}, y = {},g = {},result 1 is {}, result 2 is {}".format(x, y, g, result1, result2))
                        flag = 1
                        break
        if not flag:
            print("test ended good! your function is associative you can use PPC!!!")

    def Export_MS_Truth_Table(self, row_inputs, col_inputs, Path_MS_Table):
        """This function Exports your MS truth table
         inputs -
            Row inputs - list of your row boolean MS inputs
            Col inputs - list of your col boolean MS inputs
            Path_MS_Table - where would you like to save your truth table
         outputs - a csv of the truth table
         Example:
             import Meta_Stable
             M = Meta_Stable.Meta_Stable('/Users/tomerhershkovitz/Google_Drive/BGU_studies/Moti/Diamond_func.csv')
             M.Export_MS_Truth_Table(M.MS_Input,M.MS_Input,'/Users/tomerhershkovitz/Google_Drive/BGU_studies/Moti')
         """
        row_length = row_inputs.__len__();
        col_length = col_inputs.__len__();
        z = [[[0, 0] for x in range(col_length)] for y in range(row_length)]
        for i, x in enumerate(row_inputs):
            for j, y in enumerate(col_inputs):
                z[i][j] = self.F_closer(x + y)
        with open('{}/MS_Truth_table.csv'.format(Path_MS_Table), 'w') as F:
            F.write(',')
            F.write('{}\n'.format(col_inputs).replace(',', ' ').replace(']', '],').replace('[', '').replace(']', '').replace("'M'", 'M').replace('0', 'False').replace('1', 'True'))
            for i in range(row_length):
                F.write('{}'.format(row_inputs[i]).replace(',', ' ').replace(']', '],').replace('[', '').replace(']', '').replace("'M'", 'M').replace('0', 'False').replace('1', 'True'))
                for k in range(col_length):
                    F.write('{}'.format(z[i][k]).replace(",",' ') + ',')
                F.write('\n')
            print('\n')

    def Create_RG(self, n):
        """This function Creates a strings of gray code by order
                 inputs - number of bits
                 outputs - list of strings
                 Example:
                     import Meta_Stable
                     M = Meta_Stable.Meta_Stable('/Users/tomerhershkovitz/Google_Drive/BGU_studies/Moti/Diamond_func.csv')
                     M.Create_RG(3)
                     output:['000', '001', '011', '010', '110', '111', '101', '100']
                 """
        if n <= 0:
            return []
        if n == 1:
            return ['0', '1']
        res = self.Create_RG(n - 1)
        return ['0' + s for s in res] + ['1' + s for s in res[::-1]]


    def xor_c(self,a, b):
        return '0' if (a == b) else '1';

    # Helper function to flip the bit
    def flip(self,c):
        return '1' if (c == '0') else '0';


    # function to convert binary string
    # to gray string
    def binarytoGray(self,binary):
        """This function is a binary to gray converter
                 inputs - list of binary
                 outputs - list of gray
                 Example:
                     import Meta_Stable
                     M = Meta_Stable.Meta_Stable('/Users/tomerhershkovitz/Google_Drive/BGU_studies/Moti/Diamond_func.csv')
                     M.binarytoGray([1,0])
                     output:[1, 1]
                 """
        binary = ''.join([str(int(x)) for x in binary])
        gray = "";

        # MSB of gray code is same as
        # binary code
        gray += binary[0];

        # Compute remaining bits, next bit
        # is comuted by doing XOR of previous
        # and current in Binary
        for i in range(1, len(binary)):
            # Concatenate XOR of previous
            # bit with current bit
            gray += self.xor_c(binary[i - 1],
                          binary[i]);

        return [int(x) for x in gray];


    # function to convert gray code
    # string to binary string
    def graytoBinary(self,gray):
        """This function is a binary to gray converter
                 inputs - list of gray
                 outputs - list of binary
                 Example:
                     import Meta_Stable
                     M = Meta_Stable.Meta_Stable('/Users/tomerhershkovitz/Google_Drive/BGU_studies/Moti/Diamond_func.csv')
                     M.graytoBinary([1,1])
                     output:[1, 0]
                 """
        if self.Insertion_Format == 'Binary':   ##if this condition hold, it is not realy gray code but binary,simply return it
            return gray
        gray = ''.join([str(int(x)) for x in gray])
        binary = ""

        # MSB of binary code is same
        # as gray code
        binary += gray[0]

        # Compute remaining bits
        for i in range(1, len(gray)):

            # If current bit is 0,
            # concatenate previous bit
            if (gray[i] == '0'):
                binary += binary[i - 1]

                # Else, concatenate invert
            # of previous bit
            else:
                binary += self.flip(binary[i - 1])

        return [int(x) for x in binary]



