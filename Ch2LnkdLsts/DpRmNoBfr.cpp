
//O(n^2)


#include <iostream>
#include "LinkedList.h"

using namespace std;

void removeDups(LinkedList* ll){
	if(ll->head==NULL || ll->head->next == NULL){
		return;
	}else{
		Node* current = ll->head;
		while(current != NULL){
			Node* runner = current;
			while(runner -> next!= NULL){
				if(runner -> next -> data == current -> data){
					runner -> next = runner -> next -> next;
				}else{
					runner = runner -> next;
				}
			}
			current = current->next;
		}
	}
	
}

int main(){

	LinkedList* ll = new LinkedList();
	ll->addNode(20);
	ll->addNode(10);
	ll->addNode(30);
	ll->addNode(30);
	ll->addNode(30);
	ll->addNode(20);
	ll->addNode(15);
	ll->addNode(30);

	cout << "LinkedList created with dup values\n";
	removeDups(ll);
	cout << "Duplicates removed!\n";
	ll->printList();

	return 0;
}
