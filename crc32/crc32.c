#include <stdlib.h>
#include <stdio.h>
#include <string.h>


// Timer stuff
#include <time.h>
float gettime()
{
    return (float) (clock() / CLOCKS_PER_SEC);
}

// default CRC32 polynomial
const unsigned int polynomial = 0x04C11DB7;

unsigned int crc32(char *data, int size)
{
  unsigned int r = ~0;
  void *end = data + size;

  while(data < end)
  {
    r ^= *data++;

    for(int i = 0; i < 8; i++)
    {
      unsigned int t = ~((r&1) - 1); r = (r>>1) ^ (0xEDB88320 & t);
    }
  }

  return r ^ 0xffffffff;
}

int main( int argc, char* argv[] )
{
    // ensure the correct number of parameters are used.
    if ( argc != 2 )
    {
        printf("Wrong argument count %d", argc);
        return 1;
    }
    char* data = argv[1];
    size_t length = strlen(data);
    printf("Given Value: \"%s\", Length: %ld\n", data, length);

    //
    int runs = 100000;
    unsigned int crc = crc32(data, length);
    unsigned int prevCrc = crc;
    clock_t tickSum;
    for (int i = 0; i < runs; i++) {
        clock_t start = clock();
        crc = crc32(data, length);
        clock_t end = clock();
        if (crc != prevCrc) {
            printf("CRC values different: 0x%08x != 0x%08x", crc, prevCrc);
        }
        tickSum += end - start;
    }
    printf("CRC32: 0x%08x in %ld ticks\n", crc, tickSum / runs);

    return 0;
}