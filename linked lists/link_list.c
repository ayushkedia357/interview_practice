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
void delete(node** head,int pos){
	node* temp1=*head;
	node* temp2=*head;
	if(pos==1){
		temp2=temp2->next;
		*head=temp2;
		temp1->next=NULL;
		free(temp1);
		return;
	}
	int k=0;
	while(k<pos-2){
		temp1=temp1->next;
		k++;
	}
	temp2=temp1->next;
	temp1->next=temp2->next;
	temp2->next=NULL;
	free(temp2);
	return;
}
int main(){
	node* head=NULL;
	int a,l=0,pos;
	//printf("enter 1=>insert	2=>delete 3=>print 4=>stop:  \n");
	int choice;
	while(1){
		printf("enter 1=>insert	2=>delete 3=>print 4=>stop:  \n");
		scanf("%d",&choice);
		switch(choice){
			case 1:printf("enter the value:  ");
				   scanf("%d",&a);
				   printf("enter the pos:  ");
				   scanf("%d",&pos);
				   insert(&head,a,pos);
				   l++;
				   break;
			case 2:printf("position to be deleted?	\n");
				   scanf("%d",&pos);
				   if(pos>l){
				   	break;
				   }
				   delete(&head,pos);
				   l--;
				   break;
			case 3:print_list(head);
				   printf("\n");
				   break;
			case 4:return;
			default:return;
		}
	}
	return 0;
}
