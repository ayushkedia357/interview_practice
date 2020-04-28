#include<stdio.h>
#include<stdlib.h>
typedef struct node{//defining node
	char val;
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
		printf("%c",temp->val);
		temp=temp->next;
	}
	return;
}
void delete_mid_node(node** temp){
	node* temp1=*temp;
	node* temp2;
	temp2=temp1->next;
	while(temp2->next!=NULL){
		temp1->val=temp2->val;
		temp1=temp2;
		temp2=temp2->next;
	}
	temp1->val=temp2->val;
	temp1->next=NULL;
	free(temp2);
	return;
}
int main(){
	node* head=NULL;
	int l=0,pos;
	char a;
	//printf("enter 1=>insert	2=>delete 3=>print 4=>stop:  \n");
	int choice;
	while(1){
		printf("enter 1=>insert	2=>delete middle node  \n");
		scanf("%d",&choice);
		if(choice==2){
			break;
		}
		printf("enter the value:  ");
		scanf("%s",&a);
		printf("enter the pos:  ");
		scanf("%d",&pos);
		if(pos-1>l){
			printf("invalid input");
			continue;
		}
		insert(&head,a,pos);
		l++;
	}
	if(l==1){
		free(head);
		printf("None");
		return;
	}
	l=(l/2);
	node *temp=head;
	while(l!=0){
		temp=temp->next;
		l--;
	}
	delete_mid_node(&temp);
	print_list(head);
	return 0;
}
