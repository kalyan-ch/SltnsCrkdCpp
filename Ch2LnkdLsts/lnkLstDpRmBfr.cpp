#include <iostream>
#include <vector>
#include <algorithm>
#include "LinkedList.h"

//O(n)

void removeDups(LinkedList* ll){
	//buffer
	vector<int> myvector;
	vector<int>::iterator it;

	
	if(ll->head==NULL || ll->head->next == NULL){
		return;
	}else{
		Node* n = ll->head;
		while(n!=NULL){
			it = find (myvector.begin(), myvector.end(), 30);
			//if in buffer
			if (it != myvector.end()){
				//delete
				ll->deleteNode(n->data);
			}else{
				//or add it
				myvector.push_back(n->data);
			}

			n=n->next;
		}
	}
}

int main()
{
	
	LinkedList* ll = new LinkedList();
	ll->addNode(20);
	ll->addNode(10);
	ll->addNode(30);
	ll->addNode(30);
	ll->addNode(30);
	ll->addNode(20);
	ll->addNode(15);
	ll->addNode(30);
	cout<<"Successfully added"<<"\n";
	ll->printList();
	
	removeDups(ll);
	
	
	cout<< "Duplicates Removed!" << "\n";
	ll->printList();



	
	return 0;
}