import os
import csv
os.system('clear')


# Open the file in read mode
with open('portfolio/flow_chart/flow_charts_for_writing/velocity_project/deep_dive.txt', 'r') as file:
    lines = file.readlines()


split_lines = [(line).strip().lower().split(' ') for line in lines]

# Converting our text file into a dictionary so we can reference destination (target) nodes
# from their source node.
# This is key for creating records with the same path id so they can be paired together with
# a scatter plot displaying as a line to create the edge between nodes.
node_map = {}
nodes_for_csv = []

for line in split_lines:
    node_id = int(line[0])
    node_type = line[1].lower()
    node_name = line[2].lower()
    targets = line[3:]

    node_map[node_id] = {
        'node_id': node_id,
        'node_type': node_type,
        'node_name': node_name,
        'targets': targets,
        'is_root': True if node_type == 'start' else False,
        'is_end': True if node_type == 'end' else False
    }


# We could get far more sophisticated here, but the juice isn't worth the squeeze.  The point is to save time.
# If I ever decide to take this to market (highly unlikely), it would require far more effort.  So what I am doing here
# is ensuring that my node placements never overlap.  We just make sure that every new node level is more to the right than the last node
# level placed.  If it is a split, we just adjust each x so they don't overlap.
max_x = 0
edge_id = 0
# mapping back through creating source/destination record pairs
for node in node_map.values():
    if node['node_type'] == 'start':
        node['x'] = max_x
        node['y'] = 1000
    x = node['x']
    y = node['y']
    # the path ends
    if node['node_type'] == 'end':
        continue
    # Make sure any new nodes are on their own row
    if int(node['targets'][0]) > node['node_id']:
        max_x += 2
    for idx, target in enumerate(node['targets']):     
        target_node = node_map[int(target)]
        # The following section sets the node position for the target node.
        # If the target node has a lower id than the current node, it's position is already set.
        if int(target) > node['node_id']:
            target_node['x'] = max_x
            node_type = node['node_type']
            if node_type != 'split':
                target_node['y'] = y
            elif idx == 0:
                target_node['y'] = y - 2
            else:
                target_node['y'] = y + 2
     
        # This works fine if we aren't flowing back to a previous node, but need a better route if we aren't.
        if node['node_id'] < int(target):
            nodes_for_csv.append([
                edge_id, 
                node['node_type'],
                node['node_name'],
                str(node['x']),
                str(node['y']),
                '0'
            ])
            nodes_for_csv.append([
                edge_id,
                target_node['node_type'],
                target_node['node_name'],
                str(target_node['x']),
                str(target_node['y']),
                '1'
            ])
            edge_id += 1
        else:
            n_x = node['x']
            n_y = node['y']
            t_x = target_node['x']
            t_y = target_node['y']
            nodes_for_csv.append([
                edge_id, 
                node['node_type'],
                node['node_name'],
                str(n_x),
                str(n_y),
                '0'
            ])
            nodes_for_csv.append([
                edge_id,
                'guide',
                '',
                str(n_x),
                str(n_y + 1),
                '1'
            ])
            edge_id += 1
            nodes_for_csv.append([
                edge_id,
                'guide',
                '',
                str(n_x),
                str(n_y + 1),
                '0'
            ])
            nodes_for_csv.append([
                edge_id,
                'guide',
                '',
                str(t_x),
                str(n_y + 1),
                '1'
            ])
            edge_id += 1
            nodes_for_csv.append([
                edge_id,
                'guide',
                '',
                str(t_x),
                str(n_y + 1),
                '0'
            ])
            nodes_for_csv.append([
                edge_id,
                target_node['node_type'],
                target_node['node_name'],
                str(t_x),
                str(t_y),
                '1'
            ])
            edge_id += 1


headers = ['edge_id', 'type', 'name', 'x', 'y', 'weight']
csv_list = [headers] + nodes_for_csv

with open('portfolio/flow_chart/flow_charts_for_writing/velocity_project/deep_dive.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_list)
