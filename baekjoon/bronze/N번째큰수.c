#include<stdio.h>
#include<stdlib.h>
#define MAXN ((int)1e3)

int A[MAXN+10];

int comp(const void* a, const void* b){
    return *(int *)b - *(int *)a;
}

void InputData(){
    for(int i=0; i<10; i++) scanf("%d", &A[i]);
}

int main(){
    int T;
    scanf("%d", &T);
    for(int t=0; t<T; t++){
        InputData();

        qsort(A, 10, sizeof(A[0]), comp);
        printf("%d\n", A[2]);
    }
    return 0;
}