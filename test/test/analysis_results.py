import _init_paths
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [8, 8]

from lib.test.analysis.plot_results import plot_results, print_results, print_per_sequence_results
from lib.test.evaluation import get_dataset, trackerlist

trackers = []


# """DFDT"""
# dataset_name = 'ptbtir'
# trackers.extend(trackerlist(name='DFDT', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='ours'))
# trackers.extend(trackerlist(name='VITAL', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='VITAL'))
# trackers.extend(trackerlist(name='DSST', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='DSST'))
# trackers.extend(trackerlist(name='KCF', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='KCF'))
# trackers.extend(trackerlist(name='Staple', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='Staple'))
# trackers.extend(trackerlist(name='ECO_tir', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='ECO_tir'))
# trackers.extend(trackerlist(name='MDNet', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='MDNet'))
# trackers.extend(trackerlist(name='DSNet-Mix-46', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='DSNet-Mix-46'))
# trackers.extend(trackerlist(name='HSSNet', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='HSSNet'))
# trackers.extend(trackerlist(name='MLSSNet', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='MLSSNet'))
# trackers.extend(trackerlist(name='DSNet-VID-48', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='DSNet-VID-48'))
# trackers.extend(trackerlist(name='DSiam', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='DSiam'))
# trackers.extend(trackerlist(name='HCF', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='HCF'))
# trackers.extend(trackerlist(name='CREST', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='CREST'))
# trackers.extend(trackerlist(name='HDT', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='HDT'))
# trackers.extend(trackerlist(name='ECO_HC', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='ECO_HC'))
# trackers.extend(trackerlist(name='TADT', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='TADT'))
# trackers.extend(trackerlist(name='MCCT', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='MCCT'))
# trackers.extend(trackerlist(name='SRDCF', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='SRDCF'))
# trackers.extend(trackerlist(name='SiamFC_tri', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='SiamFC_tri'))
# trackers.extend(trackerlist(name='CFNet', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='CFNet'))
# trackers.extend(trackerlist(name='MCFTS', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='MCFTS'))
# trackers.extend(trackerlist(name='DeepSTRCF', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='DeepSTRCF'))
# trackers.extend(trackerlist(name='Siamese_FC', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='Siamese_FC'))
# trackers.extend(trackerlist(name='RidgeRegression', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='RidgeRegression'))
# trackers.extend(trackerlist(name='UDT', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='UDT'))
# trackers.extend(trackerlist(name='ECO', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='ECO'))
# trackers.extend(trackerlist(name='SVM', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='SVM'))








# dataset_name = 'lsotbtir120'
# """DFDT"""
# # trackers.extend(trackerlist(name='DFDT', parameter_name='vitb_256_mae_ce_32x4_ep300', dataset_name=dataset_name,
# #                             run_ids=None, display_name='DFDT256'))
# trackers.extend(trackerlist(name='DFDT', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='ours'))
# trackers.extend(trackerlist(name='VITAL', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='VITAL'))
# trackers.extend(trackerlist(name='DSST', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='DSST'))
# trackers.extend(trackerlist(name='SiamRPN++', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='SiamRPN++'))
# trackers.extend(trackerlist(name='Staple', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='Staple'))
# trackers.extend(trackerlist(name='ECO_tir', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='ECO_tir'))
# trackers.extend(trackerlist(name='MDNet', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='MDNet'))
# trackers.extend(trackerlist(name='CFNet_TIR', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='CFNet_TIR'))
# trackers.extend(trackerlist(name='HSSNet', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='HSSNet'))
# trackers.extend(trackerlist(name='MLSSNet', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='MLSSNet'))
# trackers.extend(trackerlist(name='HSSNet_TIR', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='HSSNet_TIR'))
# trackers.extend(trackerlist(name='HCF', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='HCF'))
# trackers.extend(trackerlist(name='CREST', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='CREST'))
# trackers.extend(trackerlist(name='HDT', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='HDT'))
# trackers.extend(trackerlist(name='ECO_HC', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='ECO_HC'))
# trackers.extend(trackerlist(name='TADT', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='TADT'))
# trackers.extend(trackerlist(name='BACF', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='BACF'))
# trackers.extend(trackerlist(name='MCCT', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='MCCT'))
# trackers.extend(trackerlist(name='SRDCF', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='SRDCF'))
# trackers.extend(trackerlist(name='SiamFC_tri', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='SiamFC_tri'))
# trackers.extend(trackerlist(name='ATOM', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='ATOM'))
# trackers.extend(trackerlist(name='SiamMask', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='SiamMask'))
# trackers.extend(trackerlist(name='CFNet', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='CFNet'))
# trackers.extend(trackerlist(name='MCFTS', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='MCFTS'))
# trackers.extend(trackerlist(name='Siamese_FC_TIR', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='Siamese_FC_TIR'))
# trackers.extend(trackerlist(name='ECO_deep_TIR', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='ECO_deep_TIR'))
# trackers.extend(trackerlist(name='ECO_deep', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='ECO_deep'))
# trackers.extend(trackerlist(name='Siamese_FC', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='Siamese_FC'))
# trackers.extend(trackerlist(name='UDT', parameter_name='vitb_384_mae_ce_32x4_ep300', dataset_name=dataset_name, run_ids=None, display_name='UDT'))


dataset = get_dataset(dataset_name)
# dataset = get_dataset('otb', 'nfs', 'uav', 'tc128ce')
# plot_results(trackers, dataset, 'OTB2015', merge_results=True, plot_types=('success', 'norm_prec'),
#              skip_missing_seq=False, force_evaluation=True, plot_bin_gap=0.05)
print_results(trackers, dataset, dataset_name, merge_results=True, plot_types=('success', 'norm_prec', 'prec'))
# print_results(trackers, dataset, 'UNO', merge_results=True, plot_types=('success', 'prec'))
