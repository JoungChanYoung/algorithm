#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAXN ((int)1e5)

char stk[MAXN+10];
int N;
int sp;

void push(char c){
    stk[++sp] = c;
}
void pop(){
    sp--;
}
char top(){
    return stk[sp];
}
int empty(){
    return sp == 0;
}
int size(){
    return sp;
}

int Solve(char* w){ 
    memset(stk, 0, sizeof(stk));
    sp = 0;
    push(w[0]);
    for (int i=1; i<strlen(w);i++){ //sizeof(w)를 사용하면 w가 포인터이기때문에 32bit환경에서 4로 고정되어나온다 -> 에러발생
        if(w[i] == top()) {
            pop();
            continue;
        }
        push(w[i]);
    }
    return empty();
}

int main(){
    int T;
    int cnt = 0;    
    scanf("%d", &T);
    char word[T][MAXN + 10];

    for(int t=0; t<T; t++){
        scanf("%s", &word[t]);
    }
    
    for(int t=0; t<T; t++){
        if (Solve(word[t])) cnt++;
    }
    printf("%d", cnt);

    return 0;
}