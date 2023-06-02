import omni.kit
import omni.replicator.core as rep
import omni.usd as usd

NUM_LIGHTS = 1

usd_file = "omniverse://localhost/NVIDIA/Assets/Isaac/2022.2.0/Isaac/People/Characters/original_male_adult_construction_05/male_adult_construction_05.usd"

omni.kit.stage_templates.new_stage(template="Puddles") 
usd.get_context().open_stage(usd_file)

# Create a new layer to perform our Replicator changes in
with rep.new_layer():
    # Find the 'cart' object and store it for later
    #cart = rep.get.prims(path_pattern="/Root/SM_PushcartA_02_22", prim_types=["Xform"])

    hat = rep.get.prims(path_pattern="/World/ManRoot/male_adult_construction_05/male_adult_construction_05/opaque__plastic__hardhat", prim_types=["Mesh"])

    # Add semantic class data to the cart
    with hat:
        rep.modify.semantics([("class", "hat")])

    # Create a camera
    camera = rep.create.camera(position=(-15, -10, 5), look_at=hat)

    with rep.trigger.on_frame(num_frames=10):
        with camera:
            rep.modify.pose(
                position=rep.distribution.uniform((-8.0, -11.5, 1), (8.5, 17, 5.5)),
                look_at=hat,
            )

    render_product = rep.create.render_product(camera, (1024, 1024))


    # Create a BasicWriter
    writer = rep.WriterRegistry.get("BasicWriter")
    # Initialize writer with output directory and all AOV/ground-truth outputs needed
    writer.initialize(
        output_dir="replicator_output_hat_104",
        rgb=True,
        bounding_box_2d_tight=True,
        bounding_box_2d_loose=True,
        semantic_segmentation=True,
        instance_segmentation=True,
        distance_to_camera=True,
        distance_to_image_plane=True,
        bounding_box_3d=True,
        occlusion=True,
        normals=True,
    )
    # Attach render_product to the writer
    writer.attach([render_product])

    # Run the simulation graph
    rep.orchestrator.run()
