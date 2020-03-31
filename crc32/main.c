#include <stdio.h>
#include <string.h>

int main(int argc, char *argv[]) {
    extern unsigned int crc32();

    char* data = argv[1];
    size_t length = strlen(data);

    unsigned int a = crc32(data, length);
    printf("0x%08x\n", a);
}