import os 
import sys 
from blockchain_parser.blockchain import Blockchain
import pymysql
import conf
import datetime

# Instantiate the Blockchain by giving the path to the directory 
# containing the .blk files created by bitcoind
def parse(filepath, filename):
    target_path = "/data/result/"
    j = filename.split(".")
    add_str = j[0]

    file_blk = open(target_path + add_str + ".blk.txt",'a')
    file_trans = open(target_path + add_str + ".trans.txt",'a')
    file_input = open(target_path + add_str + ".input.txt",'a')
    file_output = open(target_path + add_str + ".output.txt",'a')

    blockchain = Blockchain(os.path.expanduser(filepath + filename))
    for block in blockchain.get_unordered_blocks():
        file_blk.write(block.hash +"\t"+ str(block.size) +"\t"+ str(block.header.version) +"\t"+ block.header.previous_block_hash +"\t"+ block.header.merkle_root 
            + "\t"+ str(block.header.timestamp) +"\t"+ str(block.header.bits) +"\t"+ str(block.header.nonce) +"\t"+ str(block.n_transactions) + "\t" + add_str + "\n")
        for tx_index,tx in enumerate(block.transactions):
            try:
                file_trans.write(block.hash + "\t" + str(tx_index) + "\t" + tx.hash + "\t" + str(tx.version) + "\t" + str(tx.locktime) + "\t" + str(tx.n_inputs) 
                     + "\t" + str(tx.n_outputs) + "\t" + str(tx.is_segwit) + "\t" + add_str + "\n")
                for input_index, input in enumerate(tx.inputs):
                    transaction_hash = input.transaction_hash
                    transaction_index = input.transaction_index
                    if tx.is_coinbase():
                        transaction_hash = "coinbase"
                        transaction_index = 0
                    file_input.write(tx.hash + "\t" + str(input.sequence_number) + "\t" + transaction_hash+ "\t" + str(transaction_index) + "\t" + add_str + "\n")
                for output_index, output in enumerate(tx.outputs):
                    address_list = []
                    for address in output.addresses:
                        address_list.append(address.address)
                    file_output.write(tx.hash + "\t" + str(output_index) + "\t" + output.type+ "\t" + ",".join(address_list)+ "\t" + str(output.value) + "\t" + add_str + "\n")
            except Exception as e:
                print(e)
    file_blk.close()
    file_trans.close()
    file_input.close()
    file_output.close()

if __name__ == "__main__":
    #filepath = sys.argv[1]
    #database(filepath)
    file_path = "/data/block/"
    file_list = os.listdir(file_path)
    file_list.sort()
    for i in file_list:
        if "blk011" in i or "blk012" in i:
            print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " " + i)
            parse(file_path, i)
            #os.remove("/mnt/" + i)
            #print(i)
