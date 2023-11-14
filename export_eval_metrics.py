print(f"Jaccard: {jaccard:1.4f} - F1: {f1:1.4f} - Recall: {recall:1.4f} - Precision: {precision:1.4f} - Acc: {acc:1.4f} - F2: {f2:1.4f}")
print("Mean FPS: ", mean_fps)
import json

data = {
    "Jaccard": jaccard,
    "F1": f1,
    "Recall": recall,
    "Precision": precision,
    "Acc": acc,
    "F2": f2,
    "Mean FPS": mean_fps,
}

# ct = datetime.datetime.now()
# ts = ct.timestamp()
# ts_str = str(ts)
file_ext = ".json"
path_to_file = "results/eval_metrics_brightcontr_model" #ts_str
path_to_file = path_to_file + file_ext

text = json.dumps(data, indent=4)
with open(path_to_file, "w") as out_file_obj:
    # write the text into the file
    out_file_obj.write(text)