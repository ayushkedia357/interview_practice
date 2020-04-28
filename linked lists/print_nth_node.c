#include<stdio.h>
#include<stdlib.h>
typedef struct node{//defining node
	int val;
	struct node* next;
}node;
void insert(node** head,int a,int pos){
	//printf("poiuy");
	node* temp=(node*)malloc(sizeof(node));
	node* temp1=*head;
	temp->val=a;
	temp->next=NULL;
	if(*head==NULL){
		//printf("poiuy");
		*head=temp;
	}
	else if(pos==1 && *head!=NULL){
		temp->next=temp1;
		*head=temp;
		return;
	}
	else{
		int t=1;
		while(t<pos-1){
			temp1=temp1->next;
			t++;
		}
		temp->next=temp1->next;
		temp1->next=temp;
	}
	return;
}
void print_list(node **head,int a){
	//printf("%d",head->val);
	node* temp=*head;
	int k=0;
	while(temp!=NULL){
		temp=temp->next;
		k++;
	}
	temp=*head;
	a=k-a;
	while(a!=0){
		temp=temp->next;
		a--;
	}
	printf("%d",temp->val);
	return;
}
int main(){
	node *head=NULL;
	int choice,a,pos,l=0;
	while(1){
		printf("enter 1=>insert	2=>print nth node from last  \n");
		scanf("%d",&choice);
		if(choice==2){
			break;
		}
		printf("enter the value:  ");
		scanf("%d",&a);
	    printf("enter the pos:  ");
		scanf("%d",&pos);
		if(pos-1>l){
			printf("invalid postion input");
			continue;
		}
		insert(&head,a,pos);
		l++;
	}
	//printf("qwewq");
	//print_list(head);
	printf("enter the nth node:  ");
	scanf("%d",&a);
	if(a>l){
		printf("invalid input");
		return;
	}
	print_list(&head,a);//print element at l-a.
}
