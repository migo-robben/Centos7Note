from AL import usdmaya
from pxr import Usd

"""
1. Create USD prim
"""
# 将Sphere 添加到AL_usdmaya_proxyShape 的 “/Kitchen_set/Sphere” prim上面去
cmds.AL_usdmaya_CreateUsdPrim("/Kitchen_set/Sphere", "Sphere", "AL_usdmaya_ProxyShape")
# 之后可以用pxrUSDExport来导出


"""
2. Layer Create Layer
"""
cmds.AL_usdmaya_LayerCreateLayer(p="AL_usdmaya_ProxyShape", open="/home/migo/Documents/Library/Sofa/SofaAsset.usd", sublayer=1)


"""
3. Layer Get Layers
"""
cmds.AL_usdmaya_LayerGetLayers("AL_usdmaya_ProxyShape", identifiers=1, used=1)
cmds.AL_usdmaya_LayerGetLayers("AL_usdmaya_ProxyShape", identifiers=1, muted=1)
cmds.AL_usdmaya_LayerGetLayers("AL_usdmaya_ProxyShape", identifiers=1, stack=1)
cmds.AL_usdmaya_LayerGetLayers("AL_usdmaya_ProxyShape", identifiers=1, sessionLayer=1)
cmds.AL_usdmaya_LayerGetLayers("AL_usdmaya_ProxyShape", identifiers=1, rootLayer=1)

"""
4. 导入proxyShape
"""
proxyShape = cmds.AL_usdmaya_ProxyShapeImport(file='/home/migo/Downloads/Kitchen_set/Kitchen_set.usd')
# unload when import
cmds.AL_usdmaya_ProxyShapeImport(file='/home/migo/Downloads/Kitchen_set/Kitchen_set.usd', unloaded=1)
cmds.AL_usdmaya_ProxyShapeImport(file='/home/migo/Downloads/Kitchen_set/Kitchen_set.usd')

# 只显示冰箱
AL_usdmaya_ProxyShapeImport -file "/home/migo/Downloads/Kitchen_set/Kitchen_set.usd" -populationMaskInclude "/Kitchen_set/Props_grp/North_grp/FridgeArea_grp/Refridgerator_1"
# 不显示冰箱
AL_usdmaya_ProxyShapeImport -file "/home/migo/Downloads/Kitchen_set/Kitchen_set.usd" -excludePrimPath "/Kitchen_set/Props_grp/North_grp/FridgeArea_grp/Refridgerator_1"
# AL_usdmaya_ProxyShapeImport会将当前选择的xform作为ProxyShape的parent xform

"""
5. ProxyShapeSelect
"""
# 按照primpath选择prim并张开transform
cmds.AL_usdmaya_ProxyShapeSelect("AL_usdmaya_ProxyShape", replace=1, pp="/Kitchen_set/Props_grp/North_grp/FridgeArea_grp/Refridgerator_1/Geom/Body/polySurface52")

"""
6. Change Variant
"""
cmds.AL_usdmaya_ChangeVariant("AL_usdmaya_ProxyShape", primPath="/Kitchen_set/Props_grp/North_grp/FridgeArea_grp/Refridgerator_1", variantSet="modelingVariant", variant="Bare")
cmds.AL_usdmaya_ChangeVariant("AL_usdmaya_ProxyShape", primPath="/Kitchen_set/Props_grp/North_grp/FridgeArea_grp/Refridgerator_1", variantSet="modelingVariant", variant="Decorated")

cmds.AL_usdmaya_TranslatePrim("AL_usdmaya_ProxyShape", fi=True, ip="/Kitchen_set/Props_grp/North_grp/FridgeArea_grp/Refridgerator_1/Geom/Body/polySurface52")
cmds.AL_usdmaya_TranslatePrim("AL_usdmaya_ProxyShape", fi=True, tp="/Kitchen_set/Props_grp/North_grp/FridgeArea_grp/Refridgerator_1/Geom/Body/polySurface52")


"""
7. Edit Usd ProxyShape
"""
import maya.cmds as cmds
from pxr import Usd, Sdf, UsdGeom
import AL.usdmaya as usdmaya

proxyShape  = cmds.AL_usdmaya_ProxyShapeImport(file='/home/migo/Documents/Library/Sofa/Sofa.geom.usd')
shape = usdmaya.ProxyShape.getByName(proxyShape[0])
stage = shape.getUsdStage()

target = stage.GetEditTargetForLocalLayer(Sdf.Find('/home/migo/Documents/Library/Sofa/Sofa.geom.usd'))
stage.SetEditTarget(target)

stage.RemovePrim('/GCA_NK_ShaFaYi_root/GCA_NK_ShaFaYi7')
cmds.refresh()

xformPrim = UsdGeom.Xform.Define(stage, '/hello')
spherePrim = UsdGeom.Sphere.Define(stage, '/hello/world')
