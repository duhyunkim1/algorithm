#include <stdio.h>
#define LEN_INPUT 20

int main(void) {
    char s1[LEN_INPUT];
    scanf("%s", &s1, LEN_INPUT);
    for (int i=0; i<strlen(s1); i++)
    {
        if (s1[i] >= 'A' && s1[i] <= 'Z')
            s1[i] += 'a' - 'A';   
        else
            s1[i] -= 'a' - 'A';
    }
    printf("%s", s1);
    return 0;
}