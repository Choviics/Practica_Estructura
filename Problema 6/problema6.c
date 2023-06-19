#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

bool safe(int *solve, int pos, int epoch) {
    for (int i = 0; i < pos; i++) {
        if (solve[i] == epoch || abs(solve[i] - epoch) == abs(i - pos)) {
            return false;
        }
    }
    return true;
}

void findsolution(int *solve, int pos, int n) {
    if (pos == n) {
        for (int i = 0; i < n; i++) {
            printf("%d ", solve[i]);
        }
        printf("\n");
    }

    for (int i = 0; i < n; i++) {
        if (safe(solve, pos, i)) {
            solve[pos] = i;
            findsolution(solve, pos + 1, n);
            solve[pos] = -1;
        }
    }
}

int main() {
    int qeen;
    printf("Ingrese la cantidad de reinas: ");
    scanf("%d", &qeen);

    int *solve = (int *)malloc(qeen * sizeof(int));
    for (int i = 0; i < qeen; i++) {
        solve[i] = -1;
    }

    findsolution(solve, 0, qeen);

    free(solve);
    return 0;
}