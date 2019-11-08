#include<stdio.h>
#include<unistd.h>
#include<sys/wait.h>

int main(){
	pid_t x;
	int n1,n2;
	x=fork();
	if(x==0){
		scanf("%d",&n1);
		scanf("%d",&n2);
		printf("Add : %d",n1+n1);
	}
	else{
		sleep(2);
		printf("lol");
	}
}
