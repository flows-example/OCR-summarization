def main(inputs: dict, context):
  rows = inputs["rows"]
  kinds = inputs["kinds"]
  x_coordinate_name = inputs["x_coordinate_name"]
  x_coordinate: list[float] = []
  x_coordinate_dict: dict[str, dict] = {}
  data_dict: dict[str, list[float]] = {}

  for kind in kinds:
    data_dict[kind] = []

  for row in rows:
    coordinate = row[x_coordinate_name]
    if coordinate is None:
      continue

    item = x_coordinate_dict[coordinate] = {}
    x_coordinate.append(coordinate)

    for kind in kinds:
      value = row[kind]
      if value is not None:
        item[kind] = value

  for coordinate in x_coordinate:
    item = x_coordinate_dict[coordinate]
    for kind in kinds:
      sub_data = data_dict[kind]
      if kind in item:
        sub_data.append(item[kind])
      else:
        sub_data.append(0)

  if "with_sum" in inputs:
    sum_data = [0 for _ in x_coordinate]
    for _, sub_data in data_dict.items():
      for i, value in enumerate(sub_data):
        sum_data[i] += value
    data_dict[inputs["with_sum"]] = sum_data

  context.output(data_dict, "data", False)
  context.output(x_coordinate, "x_coordinate", False)
  context.done()

