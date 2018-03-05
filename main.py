import sys
import model
import instance as inst


def main(args):
    exinst = inst.example_instance()
    inst.visualize_instance(exinst)
    exmodel = model.build_model(exinst)
    exmodel['model'].optimize()
    model.parse_results(exinst, exmodel['vars'][0])


if __name__ == '__main__':
    main(sys.argv)
