c:
	gcc crc32.c -o main-c

asm:
	nasm -f elf64 crc32.asm -o crc32.o && \
		gcc main.c crc32.o -o main-asm

run: c asm
ifdef val
	./main-c ${val}
	./main-asm ${val}
	./crc32.py ${val}
endif