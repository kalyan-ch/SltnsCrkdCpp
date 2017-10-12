#include <iostream>
#include "LinkedList.h"

using namespace std;

LinkedList* prtnLL(Node* head, int data){
	if(head == NULL || head->next == NULL){
		return NULL;
	}
	
	LinkedList* finalLl = new LinkedList(); 

	//search for data
	Node* n = head;
	bool flag = false;
	while(n!=NULL){
		if(n->data == data){
			flag =true;
			break;
		}
		n = n->next;
	}

	if(flag){
	    
	    cout<< "Data found" << "\n";
		LinkedList* llSmall = new LinkedList();
		LinkedList* llBig = new LinkedList();

		//split
		Node* n1 = head;
		while(n1!=NULL){
			if(n1->data < data){
				llSmall->addNode(n1->data);
			}else{
				llBig->addNode(n1->data);
			}
			n1 = n1->next;
		}

		//merge
		Node* n2 = llSmall->head;
		while(n2!=NULL){
			finalLl->addNode(n2->data);
			n2 = n2->next;
		}

		Node* n3 = llBig->head;
		while(n3!=NULL){
			finalLl->addNode(n3->data);
			n3 = n3->next;
		}

	}else{
		return NULL;
	}

	return finalLl;
	
}

int main(){
	LinkedList* ll = new LinkedList();
	ll->addNode(25);
	ll->addNode(12);
	ll->addNode(32);
	ll->addNode(35);
	ll->addNode(73);
	ll->addNode(27);
	ll->addNode(15);
	ll->addNode(42);

	cout<< "Before partitioning" << "\n" ;

	ll->printList();

	LinkedList* prtn_list = prtnLL(ll->head,32);
	if(prtn_list!=NULL){
		cout<< "After partitioning" << "\n" ;
		prtn_list->printList();
	}else{
		cout<< "Data around which the partition should happen is not found!" << "\n";
	}

	

	return 0;
}
