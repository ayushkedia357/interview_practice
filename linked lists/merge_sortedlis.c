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
void merge_2_sortlist(node** head,node **head1){
	node* temp1=*head;
	node* temp2=*head1;
	node* temp3=*head;
	int i=1;
	while(temp1!=NULL && temp2!=NULL){
		if(temp1->val>=temp2->val){
			insert(&temp3,temp2->val,i);
			temp2=temp2->next;
		}
		else{
			temp1=temp1->next;
		}
		i++;
	}
	while(temp2!=NULL){
		insert(&temp3,temp2->val,i);
		temp2=temp2->next;
		i++;
	}
	return;
}
int main(){
	node* head=NULL;
	node* head1=NULL;
	int a,l=0,pos,ll=0;
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
	while(1){
		printf("enter 1=>insert	2=>for merging the lists  \n");
		scanf("%d",&choice);
		if(choice==2){
			break;
		}
		printf("enter the value:  ");
		scanf("%d",&a);
		printf("enter the pos:  ");
		scanf("%d",&pos);
		if(pos-1>ll){
			printf("invalid input");
			continue;
		}
		insert(&head1,a,pos);
		ll++;
	}
	print_list(head);
	print_list(head1);
	merge_2_sortlist(&head,&head1);
	print_list(head);
	return 0;
}
