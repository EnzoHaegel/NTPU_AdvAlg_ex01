#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 200

int usage(char *progname) {
    printf("Usage: %s\n", progname);
    return 0;
}

int main(int argc, char *argv[])
{
    int n, k = 0;
    double p[MAX_SIZE];
    double dp[MAX_SIZE][MAX_SIZE];
    double sum = 0;

    if (argc != 1)
        return usage(argv[0]);

    scanf("%d", &n);
    if (n == 0)
        return 0;
    scanf("%d", &k);
    while (n != 0 && k != 0 && n <= MAX_SIZE && k <= MAX_SIZE) {
        for (int i = 0; i < n; i++)
            scanf("%lf", &p[i]);
        memset(dp, 0, sizeof(dp));
        dp[0][0] = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < k; j++) {
                dp[i + 1][j + 1] += dp[i][j] * p[i];
                dp[i + 1][0] += dp[i][j] * (1 - p[i]);
            }
        }
        sum = 0;
        for (int i = 0; i < k; i++)
            sum += dp[n][i];
        printf("%.5lf\n", sum);
        scanf("%d", &n);
        if (n == 0)
            return 0;
        scanf("%d", &k);
    }
    return 0;
}
