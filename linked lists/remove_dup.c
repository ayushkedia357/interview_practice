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
		printf("%d",temp->val);
		temp=temp->next;
	}
	return;
}
void delete_dup(node** head){
	node* temp2=*head;
	node* temp=*head;
	node* temp1;

	while(temp!=NULL && temp->next!=NULL){
		//printf("bvnb");
		temp2=temp;
		temp1=temp->next;
		
		while(temp1!=NULL){
			
			if(temp1->val==temp->val){
				node* temp3;
				temp3=temp1;
				//printf("poiuy");
				temp2->next=temp1->next;
				temp1=temp1->next;
				temp3->next=NULL;
				free(temp3);
			}
			else{
				temp2=temp1;
				temp1=temp1->next;
			}
			//printf("poiuy");
		}
		temp=temp->next;
		//printf("poiuy");
	}
	return;
}
int main(){
	node *head=NULL;
	int choice,a,pos;
	while(1){
		printf("enter 1=>insert	2=>delete duplicates  \n");
		scanf("%d",&choice);
		if(choice==2){
			break;
		}
		printf("enter the value:  ");
		scanf("%d",&a);
	    printf("enter the pos:  ");
		scanf("%d",&pos);
		insert(&head,a,pos);
		//l++;
	}
	//printf("qwewq");
	//print_list(head);
	delete_dup(&head);
	print_list(head);
}
