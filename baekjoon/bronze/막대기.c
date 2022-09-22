#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAXN ((int)1e5)

int stk[MAXN+10];
int N;
int sp;

void push(int h){
    stk[++sp] = h;
}
void pop(){
    sp--;
}
int top(){
    return stk[sp];
}
int empty(){
    return sp == 0;
}
int size(){
    return sp;
}

int main(){
    scanf("%d", &N);
    int A[N+1];

    for(int i=1; i<=N; i++){
        scanf("%d", &A[i]);
    }

    push(A[1]);
    for(int i=2; i<=N; i++){
        while(!empty() && top() <= A[i]) pop();
        push(A[i]);
    }
    printf("%d",size());
    return 0;
}