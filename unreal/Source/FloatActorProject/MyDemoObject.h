// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "UObject/NoExportTypes.h"
#include "MyDemoObject.generated.h"

/**
 * 
 */
UCLASS()
class FLOATACTORPROJECT_API UMyDemoObject : public UObject
{
	GENERATED_BODY()

public:
	/*
	Test callable function for Python exposure.
	@param InValue Value to test.
	@return True if the give value is greater than zero, false otherwise.
	*/
	UFUNCTION(BlueprintCallable, Category = "PythonDemo")
	bool MyFunction(const int32 InValue);

	/*
	The pure function for Python exposure.
	@return The current value of the 'PureTest' property.
	*/
	UFUNCTION(BlueprintPure, Category = "PythonDemo")
	int32 MyPureFunction() const;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "PythonDemo")
	int32 PureTest = 0;
};

