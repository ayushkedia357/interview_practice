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
void print_list(node *head){
	//printf("%d",head->val);
	node* temp=head;
	while(temp!=NULL){
		printf("%d ",temp->val);
		temp=temp->next;
	}
	return;
}
void reverse(node** head){
	node* temp=*head;
	node* temp1=NULL;
	node* temp2;
	while(temp!=NULL){
		temp2=temp->next;
		temp->next=temp1;
		temp1=temp;
		temp=temp2;
	}
	*head=temp1;
	return;
}
int main(){
	node* head=NULL;
	int a,l=0,pos;
	//printf("enter 1=>insert	2=>delete 3=>print 4=>stop:  \n");
	int choice;
	while(1){
		printf("enter 1=>insert	2=>For 2nd list  \n");
		scanf("%d",&choice);
		if(choice==2){
			break;
		}
		printf("enter the value:  ");
		scanf("%d",&a);
		printf("enter the pos:  ");
		scanf("%d",&pos);
		if(pos-1>l){
			printf("invalid input");
			continue;
		}
		insert(&head,a,pos);
		l++;
	}
	print_list(head);
	printf("\n");
	reverse(&head);
	//printf("%d",head->val);
	print_list(head);
	return 0;
}
