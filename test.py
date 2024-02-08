import pandas as pd
import matplotlib.pyplot as plt

data_str = """
[#CLIENT#] INFO: CS350 Client Version 4.2
[#CLIENT#] INFO: Reading BMP 0: cat10test.bmp | HASH = 9c7d3c5670ec9d99b531a3ed3bff77ec
[#CLIENT#] INFO: Reading BMP 1: cat1test.bmp | HASH = 0330d3de795fa2cc62bbbac23c474fc1
[#CLIENT#] INFO: Reading BMP 2: cat2test.bmp | HASH = 8abe6684fcfbebdee7004c91420b0e23
[#CLIENT#] INFO: Reading BMP 3: cat3test.bmp | HASH = 36286f67fe2b858200babf407e3a4f10
[#CLIENT#] INFO: Reading BMP 4: cat4test.bmp | HASH = 49bf78901513117169d7af4fbf478af5
[#CLIENT#] INFO: Reading BMP 5: cat5test.bmp | HASH = 684921f2f2e1cf579fa7bffcb17cf947
[#CLIENT#] INFO: Reading BMP 6: cat6test.bmp | HASH = 31f8cb07ae203256d4fc3e372e0bf26b
[#CLIENT#] INFO: Reading BMP 7: cat7test.bmp | HASH = 0678b6a97d3808c46905e28052ee748a
[#CLIENT#] INFO: Reading BMP 8: cat8test.bmp | HASH = 0220a21e8585f4c33bd98f9c99adf403
[#CLIENT#] INFO: Reading BMP 9: cat9test.bmp | HASH = 72127d2d50365c2b7f50c53d49891526
[#CLIENT#] INFO: Reading BMP 10: test1.bmp | HASH = 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] INFO: Reading BMP 11: test2.bmp | HASH = b6770726558da9722136ce84f12bfac8
[#CLIENT#] INFO: Reading BMP 12: test3.bmp | HASH = f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] INFO: Reading BMP 13: test4.bmp | HASH = 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] INFO: Reading BMP 14: test5.bmp | HASH = 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] INFO: Reading BMP 15: test6.bmp | HASH = 11552ac97535bd4433891b63ed1dd45d
[#CLIENT#] Next Req.: +0.000000000 - OP = IMG_REGISTER, OW = 1, ID = 6
[#CLIENT#] Next Req.: +0.000000000 - OP = IMG_REGISTER, OW = 1, ID = 7
[#CLIENT#] Next Req.: +0.000000000 - OP = IMG_REGISTER, OW = 1, ID = 8
[#CLIENT#] Next Req.: +0.000000000 - OP = IMG_REGISTER, OW = 1, ID = 9
[#CLIENT#] Next Req.: +0.000000000 - OP = IMG_REGISTER, OW = 1, ID = 10
[#CLIENT#] Next Req.: +0.000000000 - OP = IMG_REGISTER, OW = 1, ID = 11
[#CLIENT#] Next Req.: +0.000000000 - OP = IMG_REGISTER, OW = 1, ID = 12
[#CLIENT#] Next Req.: +0.000000000 - OP = IMG_REGISTER, OW = 1, ID = 13
[#CLIENT#] Next Req.: +0.000000000 - OP = IMG_REGISTER, OW = 1, ID = 14
[#CLIENT#] Next Req.: +0.500000000 - OP = IMG_REGISTER, OW = 1, ID = 15
[#CLIENT#] INFO: setting client port as: 2222
[#CLIENT#] INFO: setting distribution: 0
[#CLIENT#] INFO: Initiating connection...
[#CLIENT#] PREP REQ 0
INFO: Worker thread 0 (TID = 17) started!
[#WORKER#] 3211.739797 Worker Thread Alive!
[#CLIENT#] SENT REQ 0 [OPCODE = IMG_REGISTER, OW = 1, IMG_ID = 6]
[#CLIENT#] PREP REQ 1
T1 R0:3211.739721,IMG_REGISTER,1,6,0,3211.739890,3211.739890,3211.748897
Q:[]
T1 R1:3211.748692,IMG_REGISTER,1,7,1,3211.749033,3211.749033,3211.751975
Q:[]
[#CLIENT#] SENT REQ 1 [OPCODE = IMG_REGISTER, OW = 1, IMG_ID = 7]
[#CLIENT#] RESP REQ 0
[#CLIENT#] PREP REQ 2
T1 R2:3211.758881,IMG_REGISTER,1,8,2,3211.759012,3211.759012,3211.761543
Q:[]
[#CLIENT#] SENT REQ 2 [OPCODE = IMG_REGISTER, OW = 1, IMG_ID = 8]
[#CLIENT#] RESP REQ 1
[#CLIENT#] PREP REQ 3
T1 R3:3211.768174,IMG_REGISTER,1,9,3,3211.768357,3211.768357,3211.771001
Q:[]
[#CLIENT#] SENT REQ 3 [OPCODE = IMG_REGISTER, OW = 1, IMG_ID = 9]
[#CLIENT#] RESP REQ 2
[#CLIENT#] PREP REQ 4
T1 R4:3211.779120,IMG_REGISTER,1,10,4,3211.779298,3211.779298,3211.784131
Q:[]
[#CLIENT#] SENT REQ 4 [OPCODE = IMG_REGISTER, OW = 1, IMG_ID = 10]
[#CLIENT#] RESP REQ 3
[#CLIENT#] PREP REQ 5
T1 R5:3211.799519,IMG_REGISTER,1,11,5,3211.800361,3211.800361,3211.805398
Q:[]
[#CLIENT#] SENT REQ 5 [OPCODE = IMG_REGISTER, OW = 1, IMG_ID = 11]
[#CLIENT#] RESP REQ 4
[#CLIENT#] PREP REQ 6
T1 R6:3211.818155,IMG_REGISTER,1,12,6,3211.818723,3211.818723,3211.824931
Q:[]
[#CLIENT#] SENT REQ 6 [OPCODE = IMG_REGISTER, OW = 1, IMG_ID = 12]
[#CLIENT#] RESP REQ 5
[#CLIENT#] PREP REQ 7
T1 R7:3211.850883,IMG_REGISTER,1,13,7,3211.851267,3211.851267,3211.865357
Q:[]
[#CLIENT#] SENT REQ 7 [OPCODE = IMG_REGISTER, OW = 1, IMG_ID = 13]
[#CLIENT#] RESP REQ 6
[#CLIENT#] PREP REQ 8
T1 R8:3211.905722,IMG_REGISTER,1,14,8,3211.906039,3211.906039,3211.930187
Q:[]
[#CLIENT#] SENT REQ 8 [OPCODE = IMG_REGISTER, OW = 1, IMG_ID = 14]
[#CLIENT#] RESP REQ 7
[#CLIENT#] PREP REQ 9
T1 R9:3212.023256,IMG_REGISTER,1,15,9,3212.023368,3212.023368,3212.039254
Q:[]
[#CLIENT#] SENT REQ 9 [OPCODE = IMG_REGISTER, OW = 1, IMG_ID = 15]
[#CLIENT#] RESP REQ 8
[#CLIENT#] RESP REQ 9
[#CLIENT#] PREP REQ 10
[#CLIENT#] SENT REQ 10 [OPCODE = IMG_UNUSED, OW = 0, IMG_ID = 0]
This image operation is not in use
T0 R10:3212.585609,IMG_UNUSED,0,0,10,3212.585905,3212.586021,3212.586167
Q:[]
[#CLIENT#] RESP REQ 10
[#CLIENT#] ==== REPORT ====
[#CLIENT#] R[0]: Sent: 3211.739720821 Recv: 3211.758878715 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 6    ServerImgID: 0    Rejected: No HASH: 31f8cb07ae203256d4fc3e372e0bf26b
[#CLIENT#] R[1]: Sent: 3211.748691515 Recv: 3211.768172818 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 7    ServerImgID: 1    Rejected: No HASH: 0678b6a97d3808c46905e28052ee748a
[#CLIENT#] R[2]: Sent: 3211.758880745 Recv: 3211.779117187 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 8    ServerImgID: 2    Rejected: No HASH: 0220a21e8585f4c33bd98f9c99adf403
[#CLIENT#] R[3]: Sent: 3211.768174332 Recv: 3211.799516141 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 9    ServerImgID: 3    Rejected: No HASH: 72127d2d50365c2b7f50c53d49891526
[#CLIENT#] R[4]: Sent: 3211.779120010 Recv: 3211.818150274 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 10   ServerImgID: 4    Rejected: No HASH: 9f3363f0249c15163d52e60fd9544c31
[#CLIENT#] R[5]: Sent: 3211.799518731 Recv: 3211.850480196 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 11   ServerImgID: 5    Rejected: No HASH: b6770726558da9722136ce84f12bfac8
[#CLIENT#] R[6]: Sent: 3211.818154679 Recv: 3211.905403206 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 12   ServerImgID: 6    Rejected: No HASH: f2ac174476fb2be614e8ab1ae10e82f0
[#CLIENT#] R[7]: Sent: 3211.850883169 Recv: 3212.023254085 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 13   ServerImgID: 7    Rejected: No HASH: 0caaef67aee1775ffca8eda02bd85f25
[#CLIENT#] R[8]: Sent: 3211.905722098 Recv: 3212.085292794 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 14   ServerImgID: 8    Rejected: No HASH: 5597b44eaee51bd81292d711c86a3380
[#CLIENT#] R[9]: Sent: 3212.023255935 Recv: 3212.085309316 Opcode: IMG_REGISTER    OW: 1 ClientImgID: 15   ServerImgID: 9    Rejected: No HASH: 11552ac97535bd4433891b63ed1dd45d
[#CLIENT#] R[10]: Sent: 3212.585608631 Recv: 3212.586248202 Opcode: IMG_UNUSED      OW: 0 ClientImgID: 0    ServerImgID: 10   Rejected: No
"""

# Parsing the data
data = []
for line in data_str.strip().split('\n'):
    if line.startswith("T1"):
        parts = line.split(',')
        # Extract relevant data from the line
        request_time = float(parts[1])  # Assuming this is the relevant time
        operation = parts[2]  # The type of operation
        data.append([request_time, operation])

# Convert to DataFrame
data_df = pd.DataFrame(data, columns=['Request Time', 'Operation'])

# Plotting the data
plt.figure(figsize=(10, 6))
for operation in data_df['Operation'].unique():
    subset = data_df[data_df['Operation'] == operation]
    plt.plot(subset['Request Time'], label=operation)

plt.xlabel('Request Number')
plt.ylabel('Request Time (s)')
plt.title('Request Time by Operation Type')
plt.legend()
plt.grid(True)
plt.show()
