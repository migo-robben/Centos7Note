// Fill out your copyright notice in the Description page of Project Settings.


#include "MyDemoLibrary.h"

bool UMyDemoLibrary::IsStructLocked(const FMyDemoStruct& InStruct) {
	return InStruct.LockCount > 0;
}

void UMyDemoLibrary::LockStruct(UPARAM(ref) FMyDemoStruct& InStruct) {
	++InStruct.LockCount;
}

void UMyDemoLibrary::UnlockStruct(UPARAM(ref) FMyDemoStruct& InStruct) {
	if (InStruct.LockCount == 0) {
		FFrame::KismetExecutionMessage(TEXT("LockCount was zero!"), ELogVerbosity::Error);
	}
	else {
		--InStruct.LockCount;
	}
}