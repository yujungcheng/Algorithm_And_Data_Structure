### tree/avl_tree
```
ycheng@nuc:/mnt/sdb/Data/learn/github/Algorithm_And_Data_Structure/tree$ ./avl_tree.py

Input value list: [7, 14, 5, 2, 12, 6, 3, 11, 15, 4, 1, 8, 10, 9, 0, 13, 16, 17]
  (7) -> insert value.        count: 0
  (7) update height to 0.        count: 1
  (7) update balance to 0.        count: 2
  (14) -> go right child. 7        count: 3
  (14) -> insert value.        count: 4
  (14) update height to 0.        count: 5
  (14) update balance to 0.        count: 6
  (7) update height to 1.        count: 7
  (7) update balance to -1.        count: 8
  (5) -> go left child. 7        count: 9
  (5) -> insert value.        count: 10
  (5) update height to 0.        count: 11
  (5) update balance to 0.        count: 12
  (7) update height to 1.        count: 13
  (7) update balance to 0.        count: 14
  (2) -> go left child. 7        count: 15
  (2) -> go left child. 5        count: 16
  (2) -> insert value.        count: 17
  (2) update height to 0.        count: 18
  (2) update balance to 0.        count: 19
  (5) update height to 1.        count: 20
  (5) update balance to 1.        count: 21
  (7) update height to 2.        count: 22
  (7) update balance to 1.        count: 23
  (12) -> go right child. 7        count: 24
  (12) -> go left child. 14        count: 25
  (12) -> insert value.        count: 26
  (12) update height to 0.        count: 27
  (12) update balance to 0.        count: 28
  (14) update height to 1.        count: 29
  (14) update balance to 1.        count: 30
  (7) update height to 2.        count: 31
  (7) update balance to 0.        count: 32
  (6) -> go left child. 7        count: 33
  (6) -> go right child. 5        count: 34
  (6) -> insert value.        count: 35
  (6) update height to 0.        count: 36
  (6) update balance to 0.        count: 37
  (5) update height to 1.        count: 38
  (5) update balance to 0.        count: 39
  (7) update height to 2.        count: 40
  (7) update balance to 0.        count: 41
  (3) -> go left child. 7        count: 42
  (3) -> go left child. 5        count: 43
  (3) -> go right child. 2        count: 44
  (3) -> insert value.        count: 45
  (3) update height to 0.        count: 46
  (3) update balance to 0.        count: 47
  (2) update height to 1.        count: 48
  (2) update balance to -1.        count: 49
  (5) update height to 2.        count: 50
  (5) update balance to 1.        count: 51
  (7) update height to 3.        count: 52
  (7) update balance to 1.        count: 53
  (11) -> go right child. 7        count: 54
  (11) -> go left child. 14        count: 55
  (11) -> go left child. 12        count: 56
  (11) -> insert value.        count: 57
  (11) update height to 0.        count: 58
  (11) update balance to 0.        count: 59
  (12) update height to 1.        count: 60
  (12) update balance to 1.        count: 61
  (14) update height to 2.        count: 62
  (14) update balance to 2.        count: 63
  (14) right rotate.        count: 64
  (11) update height to 0.        count: 65
  (14) update height to 0.        count: 66
  (12) update height to 1.        count: 67
  (11) update balance to 0.        count: 68
  (14) update balance to 0.        count: 69
  (12) update balance to 0.        count: 70
  (7) update height to 3.        count: 71
  (7) update balance to 1.        count: 72
  (15) -> go right child. 7        count: 73
  (15) -> go right child. 12        count: 74
  (15) -> go right child. 14        count: 75
  (15) -> insert value.        count: 76
  (15) update height to 0.        count: 77
  (15) update balance to 0.        count: 78
  (14) update height to 1.        count: 79
  (14) update balance to -1.        count: 80
  (12) update height to 2.        count: 81
  (12) update balance to -1.        count: 82
  (7) update height to 3.        count: 83
  (7) update balance to 0.        count: 84
  (4) -> go left child. 7        count: 85
  (4) -> go left child. 5        count: 86
  (4) -> go right child. 2        count: 87
  (4) -> go right child. 3        count: 88
  (4) -> insert value.        count: 89
  (4) update height to 0.        count: 90
  (4) update balance to 0.        count: 91
  (3) update height to 1.        count: 92
  (3) update balance to -1.        count: 93
  (2) update height to 2.        count: 94
  (2) update balance to -2.        count: 95
  (2)left rotate.        count: 96
  (2) update height to 0.        count: 97
  (4) update height to 0.        count: 98
  (3) update height to 1.        count: 99
  (2) update balance to 0.        count: 100
  (4) update balance to 0.        count: 101
  (3) update balance to 0.        count: 102
  (5) update height to 2.        count: 103
  (5) update balance to 1.        count: 104
  (7) update height to 3.        count: 105
  (7) update balance to 0.        count: 106
  (1) -> go left child. 7        count: 107
  (1) -> go left child. 5        count: 108
  (1) -> go left child. 3        count: 109
  (1) -> go left child. 2        count: 110
  (1) -> insert value.        count: 111
  (1) update height to 0.        count: 112
  (1) update balance to 0.        count: 113
  (2) update height to 1.        count: 114
  (2) update balance to 1.        count: 115
  (3) update height to 2.        count: 116
  (3) update balance to 1.        count: 117
  (5) update height to 3.        count: 118
  (5) update balance to 2.        count: 119
  (5) right rotate.        count: 120
  (1) update height to 0.        count: 121
  (2) update height to 1.        count: 122
  (4) update height to 0.        count: 123
  (6) update height to 0.        count: 124
  (5) update height to 1.        count: 125
  (3) update height to 2.        count: 126
  (1) update balance to 0.        count: 127
  (2) update balance to 1.        count: 128
  (4) update balance to 0.        count: 129
  (6) update balance to 0.        count: 130
  (5) update balance to 0.        count: 131
  (3) update balance to 0.        count: 132
  (7) update height to 3.        count: 133
  (7) update balance to 0.        count: 134
  (8) -> go right child. 7        count: 135
  (8) -> go left child. 12        count: 136
  (8) -> go left child. 11        count: 137
  (8) -> insert value.        count: 138
  (8) update height to 0.        count: 139
  (8) update balance to 0.        count: 140
  (11) update height to 1.        count: 141
  (11) update balance to 1.        count: 142
  (12) update height to 2.        count: 143
  (12) update balance to 0.        count: 144
  (7) update height to 3.        count: 145
  (7) update balance to 0.        count: 146
  (10) -> go right child. 7        count: 147
  (10) -> go left child. 12        count: 148
  (10) -> go left child. 11        count: 149
  (10) -> go right child. 8        count: 150
  (10) -> insert value.        count: 151
  (10) update height to 0.        count: 152
  (10) update balance to 0.        count: 153
  (8) update height to 1.        count: 154
  (8) update balance to -1.        count: 155
  (11) update height to 2.        count: 156
  (11) update balance to 2.        count: 157
  (8)left rotate.        count: 158
  (8) update height to 0.        count: 159
  (10) update height to 1.        count: 160
  (11) update height to 2.        count: 161
  (8) update balance to 0.        count: 162
  (10) update balance to 1.        count: 163
  (11) update balance to 2.        count: 164
  (11) right rotate.        count: 165
  (8) update height to 0.        count: 166
  (11) update height to 0.        count: 167
  (10) update height to 1.        count: 168
  (8) update balance to 0.        count: 169
  (11) update balance to 0.        count: 170
  (10) update balance to 0.        count: 171
  (12) update height to 2.        count: 172
  (12) update balance to 0.        count: 173
  (7) update height to 3.        count: 174
  (7) update balance to 0.        count: 175
  (9) -> go right child. 7        count: 176
  (9) -> go left child. 12        count: 177
  (9) -> go left child. 10        count: 178
  (9) -> go right child. 8        count: 179
  (9) -> insert value.        count: 180
  (9) update height to 0.        count: 181
  (9) update balance to 0.        count: 182
  (8) update height to 1.        count: 183
  (8) update balance to -1.        count: 184
  (10) update height to 2.        count: 185
  (10) update balance to 1.        count: 186
  (12) update height to 3.        count: 187
  (12) update balance to 1.        count: 188
  (7) update height to 4.        count: 189
  (7) update balance to -1.        count: 190
  (0) -> go left child. 7        count: 191
  (0) -> go left child. 3        count: 192
  (0) -> go left child. 2        count: 193
  (0) -> go left child. 1        count: 194
  (0) -> insert value.        count: 195
  (0) update height to 0.        count: 196
  (0) update balance to 0.        count: 197
  (1) update height to 1.        count: 198
  (1) update balance to 1.        count: 199
  (2) update height to 2.        count: 200
  (2) update balance to 2.        count: 201
  (2) right rotate.        count: 202
  (0) update height to 0.        count: 203
  (2) update height to 0.        count: 204
  (1) update height to 1.        count: 205
  (0) update balance to 0.        count: 206
  (2) update balance to 0.        count: 207
  (1) update balance to 0.        count: 208
  (3) update height to 2.        count: 209
  (3) update balance to 0.        count: 210
  (7) update height to 4.        count: 211
  (7) update balance to -1.        count: 212
  (13) -> go right child. 7        count: 213
  (13) -> go right child. 12        count: 214
  (13) -> go left child. 14        count: 215
  (13) -> insert value.        count: 216
  (13) update height to 0.        count: 217
  (13) update balance to 0.        count: 218
  (14) update height to 1.        count: 219
  (14) update balance to 0.        count: 220
  (12) update height to 3.        count: 221
  (12) update balance to 1.        count: 222
  (7) update height to 4.        count: 223
  (7) update balance to -1.        count: 224
  (16) -> go right child. 7        count: 225
  (16) -> go right child. 12        count: 226
  (16) -> go right child. 14        count: 227
  (16) -> go right child. 15        count: 228
  (16) -> insert value.        count: 229
  (16) update height to 0.        count: 230
  (16) update balance to 0.        count: 231
  (15) update height to 1.        count: 232
  (15) update balance to -1.        count: 233
  (14) update height to 2.        count: 234
  (14) update balance to -1.        count: 235
  (12) update height to 3.        count: 236
  (12) update balance to 0.        count: 237
  (7) update height to 4.        count: 238
  (7) update balance to -1.        count: 239
  (17) -> go right child. 7        count: 240
  (17) -> go right child. 12        count: 241
  (17) -> go right child. 14        count: 242
  (17) -> go right child. 15        count: 243
  (17) -> go right child. 16        count: 244
  (17) -> insert value.        count: 245
  (17) update height to 0.        count: 246
  (17) update balance to 0.        count: 247
  (16) update height to 1.        count: 248
  (16) update balance to -1.        count: 249
  (15) update height to 2.        count: 250
  (15) update balance to -2.        count: 251
  (15)left rotate.        count: 252
  (15) update height to 0.        count: 253
  (17) update height to 0.        count: 254
  (16) update height to 1.        count: 255
  (15) update balance to 0.        count: 256
  (17) update balance to 0.        count: 257
  (16) update balance to 0.        count: 258
  (14) update height to 2.        count: 259
  (14) update balance to -1.        count: 260
  (12) update height to 3.        count: 261
  (12) update balance to 0.        count: 262
  (7) update height to 4.        count: 263
  (7) update balance to -1.        count: 264

Display tree:
                              07                                
              03                              12                
      01              05              10              14        
  00      02      04      06      08      11      13      16    
                                    09                  15  17  



Inorder traverse:
['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17']

Preorder traverse:
['7', '3', '1', '0', '2', '5', '4', '6', '12', '10', '8', '9', '11', '14', '13', '16', '15', '17']

Postorder traverse:
['0', '2', '1', '4', '6', '5', '3', '9', '8', '11', '10', '13', '15', '17', '16', '14', '12', '7']

Level order traverse:
['07', '03', '12', '01', '05', '10', '14', '00', '02', '04', '06', '08', '11', '13', '16', '09', '15', '17']

Delete numbers 3
  (3) deleted, replaced by 4.        count: 265
  (5) update height to 1.        count: 266
  (5) update balance to -1.        count: 267
  (4) update height to 2.        count: 268
  (4) update balance to 0.        count: 269
  (7) update height to 4.        count: 270
  (7) update balance to -1.        count: 271

Display tree:
                              07                                
              04                              12                
      01              05              10              14        
  00      02              06      08      11      13      16    
                                    09                  15  17  



Delete numbers 4
  (4) deleted, replaced by 5.        count: 272
  (6) update height to 0.        count: 273
  (6) update balance to 0.        count: 274
  (5) update height to 2.        count: 275
  (5) update balance to 1.        count: 276
  (7) update height to 4.        count: 277
  (7) update balance to -1.        count: 278

Display tree:
                              07                                
              05                              12                
      01              06              10              14        
  00      02                      08      11      13      16    
                                    09                  15  17  



Delete numbers 5
  (5) deleted, replaced by 6.        count: 279
  (6) update height to 2.        count: 280
  (6) update balance to 2.        count: 281
  (6) right rotate.        count: 282
  (0) update height to 0.        count: 283
  (2) update height to 0.        count: 284
  (6) update height to 1.        count: 285
  (1) update height to 2.        count: 286
  (0) update balance to 0.        count: 287
  (2) update balance to 0.        count: 288
  (6) update balance to 1.        count: 289
  (1) update balance to -1.        count: 290
  (7) update height to 4.        count: 291
  (7) update balance to -1.        count: 292

Display tree:
                              07                                
              01                              12                
      00              06              10              14        
                  02              08      11      13      16    
                                    09                  15  17  



Delete numbers 0
  (1) update height to 2.        count: 293
  (1) update balance to -2.        count: 294
  (6) right rotate.        count: 295
  (6) update height to 0.        count: 296
  (2) update height to 1.        count: 297
  (1) update height to 2.        count: 298
  (6) update balance to 0.        count: 299
  (2) update balance to -1.        count: 300
  (1) update balance to -2.        count: 301
  (1)left rotate.        count: 302
  (1) update height to 0.        count: 303
  (6) update height to 0.        count: 304
  (2) update height to 1.        count: 305
  (1) update balance to 0.        count: 306
  (6) update balance to 0.        count: 307
  (2) update balance to 0.        count: 308
  (7) update height to 4.        count: 309
  (7) update balance to -2.        count: 310
  (7)left rotate.        count: 311
  (1) update height to 0.        count: 312
  (6) update height to 0.        count: 313
  (2) update height to 1.        count: 314
  (9) update height to 0.        count: 315
  (8) update height to 1.        count: 316
  (11) update height to 0.        count: 317
  (10) update height to 2.        count: 318
  (7) update height to 3.        count: 319
  (13) update height to 0.        count: 320
  (15) update height to 0.        count: 321
  (17) update height to 0.        count: 322
  (16) update height to 1.        count: 323
  (14) update height to 2.        count: 324
  (12) update height to 4.        count: 325
  (1) update balance to 0.        count: 326
  (6) update balance to 0.        count: 327
  (2) update balance to 0.        count: 328
  (9) update balance to 0.        count: 329
  (8) update balance to -1.        count: 330
  (11) update balance to 0.        count: 331
  (10) update balance to 1.        count: 332
  (7) update balance to -1.        count: 333
  (13) update balance to 0.        count: 334
  (15) update balance to 0.        count: 335
  (17) update balance to 0.        count: 336
  (16) update balance to 0.        count: 337
  (14) update balance to -1.        count: 338
  (12) update balance to 1.        count: 339

Display tree:
                              12                                
              07                              14                
      02              10              13              16        
  01      06      08      11                      15      17
```