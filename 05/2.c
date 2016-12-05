#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/md5.h>

char *str2md5(const char *str, int length) {
    int n;
    MD5_CTX c;
    unsigned char digest[16];
    char *out = (char*)malloc(33);

    MD5_Init(&c);
    MD5_Update(&c, str, length);
    MD5_Final(digest, &c);

    for (n = 0; n < 16; ++n) {
        snprintf(&(out[n*2]), 16*2, "%02x", (unsigned int)digest[n]);
    }

    return out;
}

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("Hey -- gimme a code\n");
        return 2;
    }

    char doorid[512] = "";
    char buffer[256];
    char password[8] = "--------";

    strcpy(doorid, argv[1]);
    int initial = strlen(doorid);

    int i = 0;
    int flag = 0;
    char pwd = 0;
    while (pwd < 8) {
        do {
            sprintf(buffer, "%d", i++);
            strcpy(&doorid[initial], buffer);
            //printf("->%s<-\n", doorid);
            char *output = str2md5(doorid, strlen(doorid));
            // printf("%s\n", output);
            flag = strncmp(output, "00000", 5);
            //printf("%s %d\n", output, flag);
            int position = output[5] - '0';
            if (!flag && position >= 0 && position < 8 && password[position] == '-') {
                password[position] = output[6];
                pwd++;
                free(output);
                break;
            }
            free(output);
        } while (1); 
        printf("%d %s\n", i, password);
    }

    return 0;
}
