#include<stdio.h>
#include<stdlib.h>
#define MAXN ((int)1e3)
int N;
int A[MAXN+10];

int comp(const void* a, const void* b){
    return *(int *)a - *(int *)b;
}

void InputData(){
    scanf("%d", &N);
    for(int i=0; i<N; i++) scanf("%d", &A[i]);
}

void OutputData(){
    for(int i=0; i<N; i++) printf("%d ", A[i]);
}

int main(){
    InputData();

    qsort(A, N, sizeof(A[0]), comp);

    OutputData();

    return 0;
}