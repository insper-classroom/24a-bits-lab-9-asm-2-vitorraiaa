leaw $2, %A
movw %A, %D
leaw $0, %A
movw %D, (%A)
leaw $1, %A
movw (%A), %D
leaw $2, %A
addw %D, (%A), %D
leaw $2, %A
subw %A, %D, %D
leaw $END, %A
jge %D
nop
leaw $1, %A
movw %A, %D
leaw $0, %addw
movw %D, (%A)
END: