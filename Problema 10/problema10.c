#include <stdio.h>
#include <string.h>

void getZarr(char *string, int *z) {
    int n = strlen(string);
    int l = 0, r = 0, k = 0;

    for (int i = 1; i < n; i++) {
        if (i > r) {
            l = i;
            r = i;
            while (r < n && string[r - l] == string[r]) {
                r++;
            }
            z[i] = r - l;
            r--;
        } else {
            k = i - l;
            if (z[k] < r - i + 1) {
                z[i] = z[k];
            } else {
                l = i;
                while (r < n && string[r - l] == string[r]) {
                    r++;
                }
                z[i] = r - l;
                r--;
            }
        }
    }
}

void search(char *text, char *pattern) {
    int text_len = strlen(text);
    int pattern_len = strlen(pattern);
    int concat_len = text_len + pattern_len + 1;

    char concat[concat_len];
    strcpy(concat, pattern);
    strcat(concat, "$");
    strcat(concat, text);

    int z[concat_len];
    getZarr(concat, z);

    for (int i = 0; i < concat_len; i++) {
        if (z[i] == pattern_len) {
            printf("Patrón encontrado en el índice %d\n", i - pattern_len - 1);
        }
    }
}

int main() {
    char text[1000];
    char pattern[1000];

    printf("Ingresa el texto: ");
    fgets(text, sizeof(text), stdin);
    text[strcspn(text, "\n")] = '\0';

    printf("Ingresa el patron: ");
    fgets(pattern, sizeof(pattern), stdin);
    pattern[strcspn(pattern, "\n")] = '\0';

    search(text, pattern);

    return 0;
}
