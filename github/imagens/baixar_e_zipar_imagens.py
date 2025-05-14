import os
import requests
import zipfile

# --- CONFIGURAÇÃO: coloque suas 100 URLs aqui ---
urls = [
    # conceitos_basicos
    "https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/conceitos_basicos/git_01_snapshot.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/conceitos_basicos/git_02_areas_stage.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/conceitos_basicos/git_03_directorio_trabalho.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/conceitos_basicos/git_04_staging_area.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/conceitos_basicos/git_05_local_repo.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/conceitos_basicos/git_06_hash_commit.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/conceitos_basicos/git_07_commit_lifecycle.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/conceitos_basicos/git_08_undo_changes.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/conceitos_basicos/git_09_gitignore.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/conceitos_basicos/git_10_repositorio_distribuido.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/conceitos_basicos/git_11_git_vs_svn.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/conceitos_basicos/git_12_basics_workflow.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/conceitos_basicos/git_13_local_remote.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/conceitos_basicos/git_14_ssh_https.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/conceitos_basicos/git_15_config_global.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/conceitos_basicos/git_16_gitconfig.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/conceitos_basicos/git_17_cli_commands.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/conceitos_basicos/git_18_git_gui_tools.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/conceitos_basicos/git_19_commits_comparacao.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/conceitos_basicos/git_20_revert_reset.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/conceitos_basicos/git_21_diffs.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/conceitos_basicos/git_22_log_graph.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/conceitos_basicos/git_23_tagging.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/conceitos_basicos/git_24_brief_history.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/conceitos_basicos/git_25_cheatsheet.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/push_pull/git_26_push_overview.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/push_pull/git_27_push_branch.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/push_pull/git_28_push_set_upstream.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/push_pull/git_29_pull_overview.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/push_pull/git_30_fetch_vs_pull.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/push_pull/git_31_pull_merge.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/push_pull/git_32_fast_forward.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/push_pull/git_33_push_pull_analogy.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/push_pull/git_34_http_vs_ssh.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/push_pull/git_35_auth_token.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/push_pull/git_36_https_credentials.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/push_pull/git_37_ssh_keys.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/push_pull/git_38_multiple_remotes.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/push_pull/git_39_remote_show.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/push_pull/git_40_remote_prune.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/push_pull/git_41_conflict_fetch.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/push_pull/git_42_resolve_pull_conflicts.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/push_pull/git_43_pull_request_banner.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/push_pull/git_44_ci_cd_trigger.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/push_pull/git_45_push_all_branches.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/push_pull/git_46_pull_rebase.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/push_pull/git_47_push_force.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/push_pull/git_48_push_tags.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/push_pull/git_49_pull_depth.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/push_pull/git_50_sync_forks.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/merge_branch/git_51_branch_overview.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/merge_branch/git_52_create_branch.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/merge_branch/git_53_list_branches.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/merge_branch/git_54_switch_branch.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/merge_branch/git_55_branch_naming.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/merge_branch/git_56_branch_delete.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/merge_branch/git_57_branch_merge_simple.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/merge_branch/git_58_branch_merge_conflict.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/merge_branch/git_59_merge_markers.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/merge_branch/git_60_resolve_conflict.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/merge_branch/git_61_rebase_vs_merge.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/merge_branch/git_62_interactive_rebase.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/merge_branch/git_63_squash_merge.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/merge_branch/git_64_fast_forward_merge.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/merge_branch/git_65_pull_request_flow.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/merge_branch/git_66_pr_approve_merge.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/merge_branch/git_67_pr_label_review.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/merge_branch/git_68_pr_comment.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/merge_branch/git_69_pr_conflict_ui.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/merge_branch/git_70_pr_resolve_conflict.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/merge_branch/git_71_pr_merge_options.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/merge_branch/git_72_delete_branch_post_merge.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/merge_branch/git_73_fork_pr_flow.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/merge_branch/git_74_fork_sync.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/merge_branch/git_75_remote_tracking_branch.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/fluxos_pipeline/git_76_gitflow_overview.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/fluxos_pipeline/git_77_gitflow_develop.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/fluxos_pipeline/git_78_gitflow_feature.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/fluxos_pipeline/git_79_gitflow_release.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/fluxos_pipeline/git_80_gitflow_hotfix.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/fluxos_pipeline/git_81_github_flow.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/fluxos_pipeline/git_82_trunk_based_flow.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/fluxos_pipeline/git_83_octopus_flow.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/fluxos_pipeline/git_84_ci_cd_pipeline.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/fluxos_pipeline/git_85_actions_workflow.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/fluxos_pipeline/git_86_actions_yml_structure.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/fluxos_pipeline/git_87_actions_event_triggers.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/fluxos_pipeline/git_88_actions_jobs_steps.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/fluxos_pipeline/git_89_actions_secrets.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/fluxos_pipeline/git_90_actions_matrix.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/fluxos_pipeline/git_91_actions_caching.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/fluxos_pipeline/git_92_actions_artifacts.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/fluxos_pipeline/git_93_actions_notifications.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/fluxos_pipeline/git_94_terraform_pipeline.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/fluxos_pipeline/git_95_docker_pipeline.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/fluxos_pipeline/git_96_kubernetes_deploy.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/fluxos_pipeline/git_97_codeql_scan.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/fluxos_pipeline/git_98_snyk_scan.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/fluxos_pipeline/git_99_slack_notification.png",
"https://raw.githubusercontent.com/fanaticos4tech/git-imagens/main/images/fluxos_pipeline/git_100_workflow_visualizer.png"

    # ... (total 100 URLs)
]

# Nome do arquivo ZIP que será gerado
zip_filename = "Git_Imagens_Comandos.zip"

# Pasta temporária para salvar as imagens
temp_dir = "imagens_temp"
os.makedirs(temp_dir, exist_ok=True)

print("Baixando imagens...")
for url in urls:
    local_filename = os.path.join(temp_dir, os.path.basename(url))
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        with open(local_filename, "wb") as f:
            f.write(r.content)
        print(f"  ✔ {os.path.basename(url)}")
    except Exception as e:
        print(f"  ✖ Erro ao baixar {url}: {e}")

print(f"\nCompactando em {zip_filename}...")
with zipfile.ZipFile(zip_filename, "w", compression=zipfile.ZIP_DEFLATED) as zipf:
    for root, _, files in os.walk(temp_dir):
        for file in files:
            filepath = os.path.join(root, file)
            arcname = os.path.relpath(filepath, temp_dir)
            zipf.write(filepath, arcname)

print("Limpeza temporária...")
for root, _, files in os.walk(temp_dir):
    for file in files:
        os.remove(os.path.join(root, file))
os.rmdir(temp_dir)

print(f"\nPronto! Abra o arquivo {zip_filename} na pasta atual.")
