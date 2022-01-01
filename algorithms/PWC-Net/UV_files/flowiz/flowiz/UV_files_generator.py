import flowiz as fz
from PIL import Image


out = 0

# Each loop generates a pair of UV images from each flow_file (previously generated from the datasets' images)

for i in range(232):

    a = "/path_to_flow-files_folder1/{:06d}.flo".format(i)
    b = "/path_to_output_folder1/{:06d}_x.png".format(out)
    c = "/path_to_output_folder2/{:06d}_y.png".format(out)

    out += 1

    img = fz.convert_from_file(a)

    flow = fz.read_flow(a)
    uv = fz.convert_from_flow(flow,"UV")
    Image.fromarray(uv[...,0]).save(b) 
    Image.fromarray(uv[...,1]).save(c)


out = 0

for i in range(298):

    a = "/path_to_flow-files_folder2/{:06d}.flo".format(i)
    b = "/path_to_output_folder1/{:06d}_x.png".format(out)
    c = "/path_to_output_folder2/{:06d}_y.png".format(out)

    out += 1

    img = fz.convert_from_file(a)

    flow = fz.read_flow(a)
    uv = fz.convert_from_flow(flow,"UV")
    Image.fromarray(uv[...,0]).save(b)
    Image.fromarray(uv[...,1]).save(c)


out = 0

for i in range(79):

    a = "/path_to_flow-files_folder3/{:06d}.flo".format(i)
    b = "/path_to_output_folder1/{:06d}_x.png".format(out)
    c = "/path_to_output_folder2/{:06d}_y.png".format(out)

    out += 1

    img = fz.convert_from_file(a)

    flow = fz.read_flow(a)
    uv = fz.convert_from_flow(flow,"UV")
    Image.fromarray(uv[...,0]).save(b)
    Image.fromarray(uv[...,1]).save(c)


out = 0

for i in range(99):

    a = "/path_to_flow-files_folder4/{:06d}.flo".format(i)
    b = "/path_to_output_folder1/{:06d}_x.png".format(out)
    c = "/path_to_output_folder2/{:06d}_y.png".format(out)

    out += 1

    img = fz.convert_from_file(a)

    flow = fz.read_flow(a)
    uv = fz.convert_from_flow(flow,"UV")
    Image.fromarray(uv[...,0]).save(b)
    Image.fromarray(uv[...,1]).save(c)


out = 0

for i in range(60):

    a = "/path_to_flow-files_folder5/{:06d}.flo".format(i)
    b = "/path_to_output_folder1/{:06d}_x.png".format(out)
    c = "/path_to_output_folder2/{:06d}_y.png".format(out)

    out += 1

    img = fz.convert_from_file(a)

    flow = fz.read_flow(a)
    uv = fz.convert_from_flow(flow,"UV")
    Image.fromarray(uv[...,0]).save(b)
    Image.fromarray(uv[...,1]).save(c)


out = 0

for i in range(85):

    a = "/path_to_flow-files_folder6/{:06d}.flo".format(i)
    b = "/path_to_output_folder1/{:06d}_x.png".format(out)
    c = "/path_to_output_folder2/{:06d}_y.png".format(out)

    out += 1

    img = fz.convert_from_file(a)

    flow = fz.read_flow(a)
    uv = fz.convert_from_flow(flow,"UV")
    Image.fromarray(uv[...,0]).save(b)
    Image.fromarray(uv[...,1]).save(c)


out = 0

for i in range(99):

    a = "/path_to_flow-files_folder7/{:06d}.flo".format(i)
    b = "/path_to_output_folder1/{:06d}_x.png".format(out)
    c = "/path_to_output_folder2/{:06d}_y.png".format(out)

    out += 1

    img = fz.convert_from_file(a)

    flow = fz.read_flow(a)
    uv = fz.convert_from_flow(flow,"UV")
    Image.fromarray(uv[...,0]).save(b)
    Image.fromarray(uv[...,1]).save(c)

