import numpy as np
from itertools import product
import math as m
import csv


class Assosiative:
    def __init__(self):
        self.path = '/Users/tomerhershkovitz/Google_Drive/BGU_studies/Moti/Diamond_func.csv'
        self.func_list = self._read_Bool_func_from_csv_to_func_list()
        self.MS_Input = self.generate_MS_input()
        self.Input = self.generate_input()
        self.Insertion_Format = "Gray"  ##Gray/Binary
        # self.Is_associative(self.MS_Input)
        if self.first_test():
            print("Your MS Boolean Function holds condition 1 and therefor is assosiative")
        elif self.second_test():
            print("Your MS Boolean Function holds condition 2 and therefor is assosiative")
        elif self.third_test():
            print("Your MS Boolean Function holds condition 3 and therefor is assosiative")
        else:
            print("Your MS Boolean Function failed on all 3 criterions & therefor is not neccessrly assosiative")

    # def first_test(self):
    #     for input_row in self.MS_Input:
    #         for input_col in self.MS_Input:
    #             inputs_concut = input_row + input_col
    #             Group_A = [self.func_list[self.list2ind(inputs, 'row')][self.list2ind(inputs, 'column')] for inputs in self.res(inputs_concut)]
    #             Group_B = self.res(self.star([self.func_list[self.list2ind(inputs, 'row')][self.list2ind(inputs, 'column')] for inputs in self.res(inputs_concut)]))
    #             for a in Group_A:
    #                 if [int(x) for x in a] not in Group_B:
    #                     print("1st condition not acheived here for row input {} and col input {} we receive f(res(x,y)) = {} & res(*f(res(x,y))) = {}".format(input_row,input_row,Group_A,Group_B))
    #                     return False
    #             for b in Group_B:
    #                 if [int(x) for x in b] not in Group_A:
    #                     print("1st condition not acheived here for row input {} and col input {} we receive f(res(x,y)) = {} & res(*f(res(x,y))) = {}".format(input_row,input_row,Group_A,Group_B))
    #                     return False
    #     return True

    def first_test(self):
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
        return True

    def second_test(self):
        for input_row in self.MS_Input:
            for input_col in self.MS_Input:
                inputs_concut = input_row + input_col
                A = self.star([self.func_list[self.list2ind(inputs, 'row')][self.list2ind(inputs, 'column')] for inputs in self.res(inputs_concut)])
                B = self.star(self.res(self.star([self.func_list[self.list2ind(inputs, 'row')][self.list2ind(inputs, 'column')] for inputs in self.res(inputs_concut)])))
                if A != B:
                    print("2nd condition not acheived here for row input {} and col input {} we receive *f(res(x,y)) = {} & *res(*f(res(x,y))) = {}".format(input_row,input_row,A,B))
                    return False
        return True

    def third_test(self):
        for input_row in self.MS_Input:
            for input_col in self.MS_Input:
                inputs_concut = input_row + input_col
                Group_A = self.res(self.star([self.func_list[self.list2ind(inputs, 'row')][self.list2ind(inputs, 'column')] for inputs in self.res(inputs_concut)]))
                Group_B = self.res(self.star(self.res(self.star([self.func_list[self.list2ind(inputs, 'row')][self.list2ind(inputs, 'column')] for inputs in self.res(inputs_concut)]))))
                for a in Group_A:
                    if [int(x) for x in a] not in Group_B:
                        print("1st condition not acheived here for row input {} and col input {} we receive f(res(x,y)) = {} & res(*f(res(x,y))) = {}".format(input_row,input_row,Group_A,Group_B))
                        return False
                for b in Group_B:
                    if [int(x) for x in b] not in Group_A:
                        print("1st condition not acheived here for row input {} and col input {} we receive f(res(x,y)) = {} & res(*f(res(x,y))) = {}".format(input_row,input_row,Group_A,Group_B))
                        return False
        return True
    def generate_input(self):
        return [list(x) for x in list(product([0, 1], repeat=self.func_list[0][0].__len__()))]

    def generate_MS_input(self):
        return [list(x) for x in list(product([0, 1, 'M'], repeat = self.func_list[0][0].__len__()))]

    def _read_Bool_func_from_csv_to_func_list(self):
        """No Meta stable functions are allowed here, these are for functions from
        {0,1}^n X {0,1}^m --> {0,1}^k, please insert the table in grey code order"""
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
        Sum_of_cols = [sum(x) for x in zip(*list_of_bool)]
        length = list_of_bool.__len__()
        Result = [True if v == length else False if v == 0 else 'M' for v in Sum_of_cols]
        return Result

    def dec_binary_list(self,dec_num,padding):
        return np.array([int(i) for i in list('{:0{}b}'.format(dec_num,padding))])

    def res(self,list_of_ms_inputs):
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
        return list_of_inputs

    def list2ind(self,list_of_inputs,RowOrCol):
        length = list_of_inputs.__len__()
        if RowOrCol == 'row':
            Relevent_input = list_of_inputs[0:int(length / 2)]
        else:
            Relevent_input = list_of_inputs[int(length/2):]
        Relevent_input_bin = self.graytoBinary(Relevent_input)
        return np.sum([2 ** i * x for i, x in enumerate(Relevent_input_bin[::-1])])

    def F_closer(self,inputs):
        return self.star([self.func_list[self.list2ind(inputs, 'row')][self.list2ind(inputs, 'column')] for inputs in self.res(inputs)])

    def Is_associative(self,inputs):
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

    def Export_MS_Truth_Table(self, row_inputs, col_inputs):
        row_length = row_inputs.__len__();
        col_length = col_inputs.__len__();
        z = [[[0, 0] for x in range(col_length)] for y in range(row_length)]
        for i, x in enumerate(row_inputs):
            for j, y in enumerate(col_inputs):
                z[i][j] = self.F_closer(x + y)
        with open('/Users/tomerhershkovitz/Google_Drive/BGU_studies/Moti/Truth_table.csv', 'w') as F:
            F.write(',')
            F.write('{}\n'.format(col_inputs).replace(',', ' ').replace(']', '],').replace('[', '').replace(']', '').replace("'M'", 'M').replace('0', 'False').replace('1', 'True'))
            for i in range(row_length):
                F.write('{}'.format(row_inputs[i]).replace(',', ' ').replace(']', '],').replace('[', '').replace(']', '').replace("'M'", 'M').replace('0', 'False').replace('1', 'True'))
                for k in range(col_length):
                    F.write('{}'.format(z[i][k]).replace(",",' ') + ',')
                F.write('\n')
            print('\n')

    def Create_RG(self, n):
        if n <= 0:
            return []
        if n == 1:
            return ['0', '1']
        res = self.Create_RG(n - 1)
        return ['0' + s for s in res] + ['1' + s for s in res[::-1]]

    def bin_str_to_list_of_bool(self, RG):
        return [[bool(int(x)) for x in str] for str in RG]

    # def Create_MS_RG(self, n):
    #     """At the moment only good for n=2"""
    #     RG = self.Create_RG(n)
    #     RG = self.bin_str_to_list_of_bool(RG)
    #     MS_RG = []
    #     j = 0
    #     for i in range(3**n):
    #         if i%2 == 0:
    #             MS_RG.append(RG[j])
    #         elif j < 2**n - 1:
    #             temp = RG[j].copy()
    #             temp[np.where(np.logical_xor(RG[j], RG[j+1]))[0][0]] = 'M'
    #             j = j+1
    #             MS_RG.append(temp)
    #         elif j == 2 ** n - 1:
    #             break
    #     MS_RG.append(['M' if i == 0 else False for i in range(n)])
    #     MS_RG.append(['M' for i in range(n)])
    #     return MS_RG

    def xor_c(self,a, b):
        return '0' if (a == b) else '1';

    # Helper function to flip the bit
    def flip(self,c):
        return '1' if (c == '0') else '0';


    # function to convert binary string
    # to gray string
    def binarytoGray(self,binary):
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


import Assosiative_4
A = Assosiative_4.Assosiative()
# A.Is_associative(A.c)
# A = Assosiative()
# A.Create_MS_RG(2)
