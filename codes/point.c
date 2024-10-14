#include <stdio.h>

void point(double A[], double B[], double C[], double n) {
    for (int i = 0; i < 2; i++) {
        C[i] = (A[i] + B[i] * n) / (n + 1);
    }
}

void generate_points(double A[], double B[], double result[], int num_points) {
    for (int i = 0; i < num_points; i++) {
        double t = (double)i / (num_points - 1);
        result[2 * i] = A[0] + t * (B[0] - A[0]);
        result[2 * i + 1] = A[1] + t * (B[1] - A[1]);
    }
}

