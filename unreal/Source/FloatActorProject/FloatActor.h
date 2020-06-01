// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Engine/StaticMesh.h"
#include "StaticMeshAttributes.h"
#include "RawMesh.h"
#include "MeshDescription.h"
#include "StaticMeshResources.h"
#include "AssetRegistryModule.h"
#include "FloatActor.generated.h"

UCLASS()
class FLOATACTORPROJECT_API AFloatActor : public AActor
{
	GENERATED_BODY()
	
public:	
	// Sets default values for this actor's properties
	AFloatActor();

	UPROPERTY(VisibleAnywhere)
	UStaticMeshComponent* VisualMesh;

	UPROPERTY()
	UStaticMesh *StaticMesh;

	UFUNCTION()
	void CreateStaticMesh();

	UFUNCTION()
	void CreateStaticMesh_Description();

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;

};
