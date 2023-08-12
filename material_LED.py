"""
Flashing light material node tree.
Just run this script and assign created "LED" material to your object.
Blender 3.4
Tree export by: NodeToPython add-on
Edit: O.Shcherbyna
"""



import bpy

bpy.context.scene.eevee.use_bloom = True # some scene settings
bpy.context.scene.eevee.use_ssr = True



def flashing_light_node_group():
    flashing_light= bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "Flashing Light")

    #initialize flashing_light nodes
    #node Frame
    frame = flashing_light.nodes.new("NodeFrame")
    frame.label = "Flashing = sin(frame * frequency)"

    #node Frame.002
    frame_002 = flashing_light.nodes.new("NodeFrame")
    frame_002.label = "Enable | Disable random flashing"
    frame_002.use_custom_color = True
    frame_002.color = (0.163330078125, 0.163330078125, 0.163330078125)

    #node Frame.001
    frame_001 = flashing_light.nodes.new("NodeFrame")
    frame_001.label = "Glass"

    #node Material Output
    material_output = flashing_light.nodes.new("ShaderNodeOutputMaterial")
    material_output.target = 'ALL'
    #Displacement
    material_output.inputs[2].default_value = (0.0, 0.0, 0.0)
    #Thickness
    material_output.inputs[3].default_value = 0.0

    #node Math
    math = flashing_light.nodes.new("ShaderNodeMath")
    math.operation = 'SINE'
    #Value_001
    math.inputs[1].default_value = 0.5
    #Value_002
    math.inputs[2].default_value = 0.5

    #node Math.003
    math_003 = flashing_light.nodes.new("ShaderNodeMath")
    math_003.operation = 'MULTIPLY'
    #Value_002
    math_003.inputs[2].default_value = 0.5

    #node Mix
    mix = flashing_light.nodes.new("ShaderNodeMix")
    mix.data_type = 'RGBA'
    mix.factor_mode = 'UNIFORM'
    mix.blend_type = 'MIX'
    #Factor_Float
    mix.inputs[0].default_value = 0.0
    #Factor_Vector
    mix.inputs[1].default_value = (0.5, 0.5, 0.5)
    #A_Float
    mix.inputs[2].default_value = 0.0
    #B_Float
    mix.inputs[3].default_value = 0.0
    #A_Vector
    mix.inputs[4].default_value = (0.0, 0.0, 0.0)
    #B_Vector
    mix.inputs[5].default_value = (0.0, 0.0, 0.0)
    #B_Color
    mix.inputs[7].default_value = (0.0, 0.0, 0.0, 1.0)

    #node White Noise Texture
    white_noise_texture = flashing_light.nodes.new("ShaderNodeTexWhiteNoise")
    white_noise_texture.noise_dimensions = '1D'
    #Vector
    white_noise_texture.inputs[0].default_value = (0.0, 0.0, 0.0)

    #node Math.004
    math_004 = flashing_light.nodes.new("ShaderNodeMath")
    math_004.operation = 'MULTIPLY'
    #Value_002
    math_004.inputs[2].default_value = 0.5

    #node Math.005
    math_005 = flashing_light.nodes.new("ShaderNodeMath")
    math_005.operation = 'ADD'
    #Value_002
    math_005.inputs[2].default_value = 0.5

    #node Value.001
    value_001 = flashing_light.nodes.new("ShaderNodeValue")
    value_001.label = "Frames"
    value_001.outputs[0].default_value = 0.0
    #node Group Output
    group_output = flashing_light.nodes.new("NodeGroupOutput")
    #flashing_light outputs
    
#    fcurve = flashing_light.nodes["Value"].outputs[0].driver_add("default_value")
#    fcurve.driver.type = "SCRIPTED"
#    fcurve.driver.expression = "frame"
#    bpy.data.materials["LED"].node_tree.nodes["Value"].outputs[0].default_value


    #node Principled BSDF
    principled_bsdf = flashing_light.nodes.new("ShaderNodeBsdfPrincipled")
    principled_bsdf.distribution = 'GGX'
    principled_bsdf.subsurface_method = 'RANDOM_WALK'
    #Subsurface
    principled_bsdf.inputs[1].default_value = 0.0
    #Subsurface Radius
    principled_bsdf.inputs[2].default_value = (1.0, 0.20000000298023224, 0.10000000149011612)
    #Subsurface Color
    principled_bsdf.inputs[3].default_value = (0.800000011920929, 0.800000011920929, 0.800000011920929, 1.0)
    #Subsurface IOR
    principled_bsdf.inputs[4].default_value = 1.399999976158142
    #Subsurface Anisotropy
    principled_bsdf.inputs[5].default_value = 0.0
    #Metallic
    principled_bsdf.inputs[6].default_value = 0.0
    #Specular
    principled_bsdf.inputs[7].default_value = 0.5
    #Specular Tint
    principled_bsdf.inputs[8].default_value = 0.04772727191448212
    #Roughness
    principled_bsdf.inputs[9].default_value = 0.029545456171035767
    #Anisotropic
    principled_bsdf.inputs[10].default_value = 0.0
    #Anisotropic Rotation
    principled_bsdf.inputs[11].default_value = 0.0
    #Sheen
    principled_bsdf.inputs[12].default_value = 0.0
    #Sheen Tint
    principled_bsdf.inputs[13].default_value = 0.5
    #Clearcoat
    principled_bsdf.inputs[14].default_value = 0.0
    #Clearcoat Roughness
    principled_bsdf.inputs[15].default_value = 0.029999999329447746
    #IOR
    principled_bsdf.inputs[16].default_value = 1.4500000476837158
    #Transmission
    principled_bsdf.inputs[17].default_value = 1.0
    #Transmission Roughness
    principled_bsdf.inputs[18].default_value = 0.06363636255264282
    #Alpha
    principled_bsdf.inputs[21].default_value = 1.0
    #Normal
    principled_bsdf.inputs[22].default_value = (0.0, 0.0, 0.0)
    #Clearcoat Normal
    principled_bsdf.inputs[23].default_value = (0.0, 0.0, 0.0)
    #Tangent
    principled_bsdf.inputs[24].default_value = (0.0, 0.0, 0.0)
    #Weight
    principled_bsdf.inputs[25].default_value = 0.0

    #node Group Input.001
    group_input_001 = flashing_light.nodes.new("NodeGroupInput")
    #flashing_light inputs
    #input LED Color
    flashing_light.inputs.new('NodeSocketColor', "LED Color")
    flashing_light.inputs[0].default_value = (0.08368001133203506, 0.681830883026123, 0.06891070306301117, 1.0)
    flashing_light.inputs[0].attribute_domain = 'POINT'

    #input LED Power
    flashing_light.inputs.new('NodeSocketFloat', "LED Power")
    flashing_light.inputs[1].default_value = 4.0
    flashing_light.inputs[1].min_value = 0.0
    flashing_light.inputs[1].max_value = 10000.0
    flashing_light.inputs[1].attribute_domain = 'POINT'

    #input Frequency
    flashing_light.inputs.new('NodeSocketFloat', "Frequency")
    flashing_light.inputs[2].default_value = 0.5
    flashing_light.inputs[2].min_value = 0.0
    flashing_light.inputs[2].max_value = 10000.0
    flashing_light.inputs[2].attribute_domain = 'POINT'

    #input Random On|Off 
    flashing_light.inputs.new('NodeSocketFloat', "Random On|Off ")
    flashing_light.inputs[3].default_value = 0.0
    flashing_light.inputs[3].min_value = 0.0
    flashing_light.inputs[3].max_value = 0.10000000894069672
    flashing_light.inputs[3].attribute_domain = 'POINT'



    #node Map Range
    map_range = flashing_light.nodes.new("ShaderNodeMapRange")
    map_range.data_type = 'FLOAT'
    map_range.interpolation_type = 'LINEAR'
    #From Min
    map_range.inputs[1].default_value = -1.0
    #From Max
    map_range.inputs[2].default_value = 1.0
    #To Min
    map_range.inputs[3].default_value = 0.0
    #Steps
    map_range.inputs[5].default_value = 4.0
    #Vector
    map_range.inputs[6].default_value = (0.0, 0.0, 0.0)
    #From_Min_FLOAT3
    map_range.inputs[7].default_value = (0.0, 0.0, 0.0)
    #From_Max_FLOAT3
    map_range.inputs[8].default_value = (1.0, 1.0, 1.0)
    #To_Min_FLOAT3
    map_range.inputs[9].default_value = (0.0, 0.0, 0.0)
    #To_Max_FLOAT3
    map_range.inputs[10].default_value = (1.0, 1.0, 1.0)
    #Steps_FLOAT3
    map_range.inputs[11].default_value = (4.0, 4.0, 4.0)

    #node Value
    value = flashing_light.nodes.new("ShaderNodeValue")
    value.label = "Frequency"

    value.outputs[0].default_value = 0.1
    #node Math.001
    math_001 = flashing_light.nodes.new("ShaderNodeMath")
    math_001.operation = 'MULTIPLY'
    #Value_002
    math_001.inputs[2].default_value = 0.5

    #node Fresnel
    fresnel = flashing_light.nodes.new("ShaderNodeFresnel")
    #IOR
    fresnel.inputs[0].default_value = 1.4500000476837158
    #Normal
    fresnel.inputs[1].default_value = (0.0, 0.0, 0.0)

    #node ColorRamp
    colorramp = flashing_light.nodes.new("ShaderNodeValToRGB")
    colorramp.color_ramp.color_mode = 'RGB'
    colorramp.color_ramp.hue_interpolation = 'NEAR'
    colorramp.color_ramp.interpolation = 'LINEAR'

    colorramp.color_ramp.elements.remove(colorramp.color_ramp.elements[0])
    colorramp_cre_0 = colorramp.color_ramp.elements[0]
    colorramp_cre_0.position = 0.0
    colorramp_cre_0.alpha = 1.0
    colorramp_cre_0.color = (0.0, 0.0, 0.0, 1.0)

    colorramp_cre_1 = colorramp.color_ramp.elements.new(0.04999999329447746)
    colorramp_cre_1.alpha = 1.0
    colorramp_cre_1.color = (0.9, 1.0, 1.0, 1.0)


    #node Transparent BSDF
    transparent_bsdf = flashing_light.nodes.new("ShaderNodeBsdfTransparent")
    #Color
    transparent_bsdf.inputs[0].default_value = (1.0, 1.0, 1.0, 1.0)
    #Weight
    transparent_bsdf.inputs[1].default_value = 0.0

    #node Mix Shader.001
    mix_shader_001 = flashing_light.nodes.new("ShaderNodeMixShader")

    #node Value.003
    value_003 = flashing_light.nodes.new("ShaderNodeValue")
    value_003.label = "0|1 Random flashing"

    value_003.outputs[0].default_value = 0.1
    #node Math.002
    math_002 = flashing_light.nodes.new("ShaderNodeMath")
    math_002.operation = 'GREATER_THAN'
    #Value_001
    math_002.inputs[1].default_value = 0.0010000000474974513
    #Value_002
    math_002.inputs[2].default_value = 0.5

    #node Group Input
    group_input = flashing_light.nodes.new("NodeGroupInput")

    #Set parents
    frame_002.parent = frame
    math.parent = frame
    math_003.parent = frame_002
    mix.parent = frame_002
    white_noise_texture.parent = frame_002
    math_004.parent = frame_002
    math_005.parent = frame_002
    value_001.parent = frame_002
    value.parent = frame
    math_001.parent = frame
    fresnel.parent = frame_001
    colorramp.parent = frame_001
    transparent_bsdf.parent = frame_001
    mix_shader_001.parent = frame_001
    value_003.parent = frame_002
    math_002.parent = frame_002
    group_input.parent = frame

    #Set locations
    frame.location = (168.6082763671875, -454.5994873046875)
    frame_002.location = (-876.7858276367188, -157.20831298828125)
    frame_001.location = (1060.098388671875, 783.799072265625)
    material_output.location = (1228.90576171875, 417.94952392578125)
    math.location = (-83.83480834960938, 175.26202392578125)
    math_003.location = (92.3992919921875, 122.5015869140625)
    mix.location = (-89.5386962890625, 120.43133544921875)
    white_noise_texture.location = (-88.46142578125, -109.92333984375)
    math_004.location = (93.7900390625, -42.12176513671875)
    math_005.location = (94.6798095703125, -202.15350341796875)
    value_001.location = (-86.840087890625, -252.54217529296875)
    group_output.location = (1418.90576171875, -0.0)
    principled_bsdf.location = (696.5460205078125, 422.25164794921875)
    group_input_001.location = (143.7674560546875, 207.4637451171875)
    map_range.location = (476.0464782714844, -102.99673461914062)
    value.location = (-511.12408447265625, 149.46795654296875)
    math_001.location = (-246.440185546875, 99.28005981445312)
    fresnel.location = (-524.541259765625, -17.171630859375)
    colorramp.location = (-350.28802490234375, 50.49713134765625)
    transparent_bsdf.location = (-522.3755493164062, -151.41830444335938)
    mix_shader_001.location = (-79.17324829101562, -110.15573120117188)
    value_003.location = (-636.6463012695312, 133.48458862304688)
    math_002.location = (-275.045654296875, 114.32318115234375)
    group_input.location = (-1489.600341796875, 170.38214111328125)

    #Set dimensions
    frame.width, frame.height = 1660.0, 778.5
    frame_002.width, frame_002.height = 931.5, 549.5
    frame_001.width, frame_001.height = 645.5, 340.0
    material_output.width, material_output.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    math_003.width, math_003.height = 140.0, 100.0
    mix.width, mix.height = 140.0, 100.0
    white_noise_texture.width, white_noise_texture.height = 140.0, 100.0
    math_004.width, math_004.height = 140.0, 100.0
    math_005.width, math_005.height = 140.0, 100.0
    value_001.width, value_001.height = 140.0, 100.0
    group_output.width, group_output.height = 140.0, 100.0
    principled_bsdf.width, principled_bsdf.height = 240.0, 100.0
    group_input_001.width, group_input_001.height = 140.0, 100.0
    map_range.width, map_range.height = 140.0, 100.0
    value.width, value.height = 140.0, 100.0
    math_001.width, math_001.height = 140.0, 100.0
    fresnel.width, fresnel.height = 140.0, 100.0
    colorramp.width, colorramp.height = 240.0, 100.0
    transparent_bsdf.width, transparent_bsdf.height = 140.0, 100.0
    mix_shader_001.width, mix_shader_001.height = 140.0, 100.0
    value_003.width, value_003.height = 140.0, 100.0
    math_002.width, math_002.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0

    #initialize flashing_light links
    #principled_bsdf.BSDF -> mix_shader_001.Shader
    flashing_light.links.new(principled_bsdf.outputs[0], mix_shader_001.inputs[2])
    #transparent_bsdf.BSDF -> mix_shader_001.Shader
    flashing_light.links.new(transparent_bsdf.outputs[0], mix_shader_001.inputs[1])
    #fresnel.Fac -> colorramp.Fac
    flashing_light.links.new(fresnel.outputs[0], colorramp.inputs[0])
    #colorramp.Color -> mix_shader_001.Fac
    flashing_light.links.new(colorramp.outputs[0], mix_shader_001.inputs[0])
    #value_001.Value -> white_noise_texture.W
    flashing_light.links.new(value_001.outputs[0], white_noise_texture.inputs[1])
    #map_range.Result -> principled_bsdf.Emission Strength
    flashing_light.links.new(map_range.outputs[0], principled_bsdf.inputs[20])
    #math.Value -> map_range.Value
    flashing_light.links.new(math.outputs[0], map_range.inputs[0])
    #math_002.Value -> mix.A
    flashing_light.links.new(math_002.outputs[0], mix.inputs[6])
    #mix.Result -> math_003.Value
    flashing_light.links.new(mix.outputs[2], math_003.inputs[0])
    #white_noise_texture.Value -> math_003.Value
    flashing_light.links.new(white_noise_texture.outputs[0], math_003.inputs[1])
    #math_003.Value -> math_004.Value
    flashing_light.links.new(math_003.outputs[0], math_004.inputs[0])
    #value_001.Value -> math_004.Value
    flashing_light.links.new(value_001.outputs[0], math_004.inputs[1])
    #value_001.Value -> math_005.Value
    flashing_light.links.new(value_001.outputs[0], math_005.inputs[1])
    #math_004.Value -> math_005.Value
    flashing_light.links.new(math_004.outputs[0], math_005.inputs[0])
    #math_005.Value -> math_001.Value
    flashing_light.links.new(math_005.outputs[0], math_001.inputs[1])
    #math_001.Value -> math.Value
    flashing_light.links.new(math_001.outputs[0], math.inputs[0])
    #principled_bsdf.BSDF -> material_output.Surface
    flashing_light.links.new(principled_bsdf.outputs[0], material_output.inputs[0])
    #group_input_001.LED Color -> principled_bsdf.Base Color
    flashing_light.links.new(group_input_001.outputs[0], principled_bsdf.inputs[0])
    #group_input_001.LED Color -> principled_bsdf.Emission
    flashing_light.links.new(group_input_001.outputs[0], principled_bsdf.inputs[19])
    #group_input_001.LED Power -> map_range.To Max
    flashing_light.links.new(group_input_001.outputs[1], map_range.inputs[4])
    #group_input.Frequency -> math_001.Value
    flashing_light.links.new(group_input.outputs[2], math_001.inputs[0])
    #group_input.Random On|Off  -> math_002.Value
    flashing_light.links.new(group_input.outputs[3], math_002.inputs[0])


def led_node_group(led):
    '''
    Adds a new "Flashing Light" node group to bpy.data.node_groups collection.
    '''
    group = led.nodes.new("ShaderNodeGroup")
    group.node_tree = bpy.data.node_groups["Flashing Light"]
    #Input_0
    group.inputs[0].default_value = (0.9, 0.0, 0.0, 1.0)
    #Input_1
    group.inputs[1].default_value = 18.0
    #Input_2
    group.inputs[2].default_value = 0.1
    #Input_3
    group.inputs[3].default_value = 0.0


    #Set locations
    group.location = (0.0, 0.0)

    #Set dimensions
    group.width, group.height = 237.8, 100.0



def add_driver_to_node(property, expression):
    """
    Adds a driver to node property
    """
    fcurve = property.driver_add("default_value")
    d = fcurve.driver
    d.type = "SCRIPTED"
    d.expression = expression

#create material
if "LED" not in bpy.data.materials:
    mat = bpy.data.materials.new(name = "LED")
    mat.use_nodes = True
    mat.use_screen_refraction = True # material setup, not necessary
    mat.blend_method = 'HASHED' # for Glas schader if used

#else: clean up node tree
led = bpy.data.materials["LED"].node_tree
for node in led.nodes:
    led.nodes.remove(node)

#create material node_groups
flashing_light_node_group()    
led_node_group(led)

# add driver 
add_driver_to_node(bpy.data.node_groups["Flashing Light"].nodes["Value"].outputs[0], "frame")

