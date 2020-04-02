#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-08-31 19:26:07
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-08-31 21:30:00

'''
Invalid transaction:
    1. amount > 1200
    2. With the same name but different city within 60 minutes

!!! SAT EITHER
'''


class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        names = {}
        invalids = []

        for trans in transactions:

            print(invalids)
            print(names)
            print("\n")
            print(trans)

            # Split the transcation
            trans_list = trans.split(",")
            trans_list[1] = int(trans_list[1])
            trans_list[2] = int(trans_list[2])

            if trans_list[0] not in names:
                names[trans_list[0]] = [trans]
            else:
                names[trans_list[0]].append(trans)

            # Check time
            for record in names[trans_list[0]]:
                if record == trans:
                    continue
                record_list = record.split(",")
                record_list[1] = int(record_list[1])
                # Within 60 min
                print(record + "\t" + trans)
                print(abs(trans_list[1] - record_list[1]))
                if abs(trans_list[1] - record_list[1]) <= 60:
                    # Not at the same city
                    if trans_list[3] != record_list[3]:
                        print("Within 60 min")
                        print(record + "\t" + trans)
                        invalids.append(trans)
                        if record not in invalids:
                            invalids.append(record)
            if trans_list[2] > 1000 and trans not in invalids:
                print("amount>1000" + "\t" + trans)
                invalids.append(trans)

        return invalids


if __name__ == "__main__":
    S = Solution()
    transactions = ["xnova,261,1949,chicago", "bob,206,1284,chicago", "xnova,420,996,bangkok", "chalicefy,704,1269,chicago", "iris,124,329,bangkok", "xnova,791,700,amsterdam", "chalicefy,572,697,budapest",
                    "chalicefy,231,310,chicago", "chalicefy,763,857,chicago", "maybe,837,198,amsterdam", "lee,99,940,bangkok", "bob,132,1219,barcelona", "lee,69,857,barcelona", "lee,607,275,budapest", "chalicefy,709,1171,amsterdam"]
    print(S.invalidTransactions(transactions))
