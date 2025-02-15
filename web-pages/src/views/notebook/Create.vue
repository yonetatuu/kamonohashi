<template>
  <el-dialog
    class="dialog"
    title="ノートブック起動"
    :visible.sync="dialogVisible"
    :before-close="closeDialog"
    :close-on-click-modal="false"
  >
    <kqi-display-error :error="error" />
    <!-- コピー実行 -->
    <div v-if="isCopyCreation">
      <el-form ref="runForm" :rules="rules" :model="form">
        <el-row :gutter="20">
          <div class="element">
            <el-col :span="12">
              <el-form-item label="ノートブック名" prop="name">
                <el-input v-model="form.name" />
              </el-form-item>
              <el-form-item label="インストールするJupyterLabのバージョン">
                <el-popover
                  placement="top-start"
                  width="500"
                  trigger="hover"
                  :content="jupyterLabInfo['description']"
                >
                  <i slot="reference" class="el-icon-info" />
                </el-popover>
                <el-input
                  v-model="form.jupyterLabVersion"
                  :placeholder="jupyterLabInfo['defaultVersion']"
                  clearable
                >
                </el-input>
              </el-form-item>

              <kqi-training-history-selector
                v-model="form.selectedParent"
                :histories="trainingHistories"
                multiple
              />
              <kqi-inference-history-selector
                v-model="form.selectedParentInference"
                :histories="inferenceHistories"
                multiple
              />
              <kqi-data-set-selector
                v-model="form.dataSetId"
                :data-sets="dataSets"
                @input="selectDataset"
              />
              <el-form-item
                v-show="form.dataSetId"
                label="データセット作成方式"
              >
                <el-switch
                  v-model="form.localDataSet"
                  style="width: 100%;"
                  inactive-text="シンボリックリンク"
                  active-text="ローカルコピー"
                />
              </el-form-item>
              <el-form-item label="起動時実行コマンド" prop="entryPoint">
                <el-input
                  v-model="form.entryPoint"
                  type="textarea"
                  :autosize="{ minRows: 2 }"
                />
              </el-form-item>
              <kqi-path-info :data-set="dataSetDetail" />
              <kqi-container-selector
                v-model="form.containerImage"
                :registries="registries"
                :images="images"
                :tags="tags"
                @selectRegistry="selectRegistry"
                @selectImage="selectImage"
              />
              <kqi-git-selector
                v-model="form.gitModel"
                :gits="gits"
                :repositories="repositories"
                :branches="branches"
                :commits="commitsList"
                :loading-repositories="loadingRepositories"
                @selectGit="selectGit"
                @selectRepository="selectRepository"
                @selectBranch="selectBranch"
                @searchCommitId="searchCommitId"
                @getMoreCommits="getMoreCommits"
              />
            </el-col>
            <el-col :span="12">
              <kqi-resource-selector v-model="form.resource" :quota="quota" />
              <div v-if="availableInfiniteTime">
                <el-form-item label="起動期間設定">
                  <el-switch
                    v-model="form.withExpiresInSetting"
                    style="width: 100%;"
                    inactive-text="OFF"
                    active-text="ON"
                  />
                </el-form-item>
              </div>
              <div v-show="form.withExpiresInSetting">
                <el-form-item label="起動期間(h)" required>
                  <el-slider
                    v-model="form.expiresIn"
                    class="el-input"
                    :min="1"
                    :max="100"
                    show-input
                  />
                </el-form-item>
              </div>
              <kqi-environment-variables v-model="form.variables" />
              <kqi-partition-selector
                v-model="form.partition"
                :partitions="partitions"
              />
              <el-form-item label="メモ">
                <el-input
                  v-model="form.memo"
                  type="textarea"
                  :autosize="{ minRows: 2, maxRows: 4 }"
                />
              </el-form-item>
            </el-col>
          </div>
        </el-row>
      </el-form>
    </div>
    <!-- 再実行 -->
    <div v-else-if="isReRunCreation">
      <el-row :gutter="20">
        <div class="element">
          <el-form v-if="active === 0">
            <el-col :span="12">
              <el-form-item label="インストールするJupyterLabのバージョン">
                <el-popover
                  placement="top-start"
                  width="500"
                  trigger="hover"
                  :content="jupyterLabInfo['description']"
                >
                  <i slot="reference" class="el-icon-info" />
                </el-popover>
                <el-input
                  v-model="form.jupyterLabVersion"
                  :placeholder="jupyterLabInfo['defaultVersion']"
                  clearable
                >
                </el-input>
              </el-form-item>
              <kqi-training-history-selector
                v-model="form.selectedParent"
                :histories="trainingHistories"
                multiple
              />
              <kqi-inference-history-selector
                v-model="form.selectedParentInference"
                :histories="inferenceHistories"
                multiple
              />
              <kqi-data-set-selector
                v-model="form.dataSetId"
                :data-sets="dataSets"
                @input="selectDataset"
              />
              <el-form-item
                v-show="form.dataSetId"
                label="データセット作成方式"
              >
                <el-switch
                  v-model="form.localDataSet"
                  style="width: 100%;"
                  inactive-text="シンボリックリンク"
                  active-text="ローカルコピー"
                />
              </el-form-item>
              <el-form-item label="起動時実行コマンド" prop="entryPoint">
                <el-input
                  v-model="form.entryPoint"
                  type="textarea"
                  :autosize="{ minRows: 2 }"
                />
              </el-form-item>
              <kqi-path-info :data-set="dataSetDetail" />
              <kqi-container-selector
                v-model="form.containerImage"
                :registries="registries"
                :images="images"
                :tags="tags"
                @selectRegistry="selectRegistry"
                @selectImage="selectImage"
              />
              <kqi-git-selector
                v-model="form.gitModel"
                :gits="gits"
                :repositories="repositories"
                :branches="branches"
                :commits="commitsList"
                :loading-repositories="loadingRepositories"
                @selectGit="selectGit"
                @selectRepository="selectRepository"
                @selectBranch="selectBranch"
                @searchCommitId="searchCommitId"
                @getMoreCommits="getMoreCommits"
              />
            </el-col>
            <el-col :span="12">
              <kqi-resource-selector v-model="form.resource" :quota="quota" />
            </el-col>
            <el-col :span="12">
              <div v-if="availableInfiniteTime">
                <el-form-item label="起動期間設定">
                  <el-switch
                    v-model="form.withExpiresInSetting"
                    style="width: 100%;"
                    inactive-text="OFF"
                    active-text="ON"
                  />
                </el-form-item>
              </div>
              <div v-show="form.withExpiresInSetting">
                <el-form-item label="起動期間(h)" required>
                  <el-slider
                    v-model="form.expiresIn"
                    class="el-input"
                    :min="1"
                    :max="100"
                    show-input
                  />
                </el-form-item>
              </div>
            </el-col>
          </el-form>
        </div>
      </el-row>
    </div>
    <div v-else>
      <el-row :gutter="20">
        <el-steps :active="active" align-center>
          <el-step title="Step 1" description="ノートブック名" />
          <el-step title="Step 2" description="リソース & 起動期間" />
          <el-step title="Step 3" description="任意項目" />
          <el-step title="Step 4" description="任意項目" />
        </el-steps>
        <br />
        <div class="element">
          <!-- step 1 -->
          <el-form v-if="active === 0" ref="form0" :model="form" :rules="rules">
            <el-col :span="18" :offset="3">
              <el-form-item
                label="ノートブック名"
                prop="name"
                class="is-required"
              >
                <el-input v-model="form.name" />
              </el-form-item>
            </el-col>
          </el-form>

          <!-- step 2 -->
          <el-form v-if="active === 1" ref="form1" :model="form" :rules="rules">
            <el-col :span="18" :offset="3">
              <kqi-resource-selector v-model="form.resource" :quota="quota" />
            </el-col>
            <el-col :span="18" :offset="3">
              <div v-if="availableInfiniteTime">
                <el-form-item label="起動期間設定">
                  <el-switch
                    v-model="form.withExpiresInSetting"
                    style="width: 100%;"
                    inactive-text="OFF"
                    active-text="ON"
                  />
                </el-form-item>
              </div>
              <div v-show="form.withExpiresInSetting">
                <el-form-item label="起動期間(h)" required>
                  <el-slider
                    v-model="form.expiresIn"
                    class="el-input"
                    :min="1"
                    :max="100"
                    show-input
                  />
                </el-form-item>
              </div>
            </el-col>
          </el-form>

          <!-- step 3 -->
          <el-form v-if="active === 2" ref="form2" :model="form" :rules="rules">
            <el-col :span="10" :offset="2">
              <kqi-container-selector
                v-model="form.containerImage"
                :registries="registries"
                :images="images"
                :tags="tags"
                @selectRegistry="selectRegistry"
                @selectImage="selectImage"
              />
            </el-col>
            <el-col :span="10">
              <kqi-git-selector
                v-model="form.gitModel"
                :gits="gits"
                :repositories="repositories"
                :branches="branches"
                :commits="commitsList"
                :loading-repositories="loadingRepositories"
                @selectGit="selectGit"
                @selectRepository="selectRepository"
                @selectBranch="selectBranch"
                @searchCommitId="searchCommitId"
                @getMoreCommits="getMoreCommits"
              />
            </el-col>
            <el-col :span="18" :offset="3">
              <el-form-item label="インストールするJupyterLabのバージョン">
                <el-popover
                  placement="top-start"
                  width="500"
                  trigger="hover"
                  :content="jupyterLabInfo['description']"
                >
                  <i slot="reference" class="el-icon-info" />
                </el-popover>
                <el-input
                  v-model="form.jupyterLabVersion"
                  :placeholder="jupyterLabInfo['defaultVersion']"
                  clearable
                >
                </el-input>
              </el-form-item>

              <kqi-training-history-selector
                v-model="form.selectedParent"
                :histories="trainingHistories"
                multiple
              />
              <kqi-inference-history-selector
                v-model="form.selectedParentInference"
                :histories="inferenceHistories"
                multiple
              />
              <kqi-data-set-selector
                v-model="form.dataSetId"
                :data-sets="dataSets"
                @input="selectDataset"
              />
              <el-form-item
                v-show="form.dataSetId"
                label="データセット作成方式"
              >
                <el-switch
                  v-model="form.localDataSet"
                  style="width: 100%;"
                  inactive-text="シンボリックリンク"
                  active-text="ローカルコピー"
                />
              </el-form-item>
            </el-col>
          </el-form>

          <!-- step 4 -->
          <el-form v-if="active === 3" ref="form3" :model="form" :rules="rules">
            <el-col>
              <el-form-item label="起動時実行コマンド" prop="entryPoint">
                <el-input
                  v-model="form.entryPoint"
                  type="textarea"
                  :autosize="{ minRows: 2 }"
                />
              </el-form-item>
              <kqi-path-info :data-set="dataSetDetail" />
              <kqi-environment-variables v-model="form.variables" />
              <kqi-partition-selector
                v-model="form.partition"
                :partitions="partitions"
              />
              <el-form-item label="メモ">
                <el-input
                  v-model="form.memo"
                  type="textarea"
                  :autosize="{ minRows: 2, maxRows: 4 }"
                />
              </el-form-item>
            </el-col>
          </el-form>
        </div>
      </el-row>
    </div>
    <el-row class="step">
      <div v-if="isCopyCreation || isReRunCreation">
        <span class="right-step-group">
          <el-button @click="emitCancel">キャンセル</el-button>
          <el-button type="primary" @click="runNotebook">起動 </el-button>
        </span>
      </div>
      <div v-else>
        <span
          v-if="active >= 1"
          class="left-step-group"
          style="margin-top: 12px;"
          @click="previous"
        >
          <i class="el-icon-arrow-left" />
          Previous step
        </span>
        <span
          v-if="active <= 2"
          class="right-step-group"
          style="margin-top: 12px;"
          @click="next"
        >
          Next step
          <i class="el-icon-arrow-right" />
        </span>
        <span class="right-step-group">
          <el-button v-if="active === 3" type="primary" @click="runNotebook">
            起動
          </el-button>
        </span>
      </div>
    </el-row>
  </el-dialog>
</template>

<script>
import KqiDisplayError from '@/components/KqiDisplayError'
import KqiDataSetSelector from '@/components/selector/KqiDataSetSelector'
import KqiTrainingHistorySelector from '@/components/selector/KqiTrainingHistorySelector'
import KqiInferenceHistorySelector from '@/components/selector/KqiInferenceHistorySelector'
import KqiContainerSelector from '@/components/selector/KqiContainerSelector'
import KqiGitSelector from '@/components/selector/KqiGitSelector'
import KqiResourceSelector from '@/components/selector/KqiResourceSelector'
import KqiPathInfo from '@/components/KqiPathInfo'
import KqiEnvironmentVariables from '@/components/KqiEnvironmentVariables'
import KqiPartitionSelector from '@/components/selector/KqiPartitionSelector'
import registrySelectorUtil from '@/util/registrySelectorUtil'
import gitSelectorUtil from '@/util/gitSelectorUtil'
import { mapActions, mapGetters } from 'vuex'

export default {
  components: {
    KqiDisplayError,
    KqiDataSetSelector,
    KqiTrainingHistorySelector,
    KqiInferenceHistorySelector,
    KqiResourceSelector,
    KqiContainerSelector,
    KqiGitSelector,
    KqiPathInfo,
    KqiEnvironmentVariables,
    KqiPartitionSelector,
  },
  props: {
    originId: {
      type: String,
      default: null,
    },
  },
  data() {
    return {
      commitsList: [],
      commitsPage: 1,
      form: {
        name: null,
        dataSetId: null,
        selectedParent: [],
        selectedParentInference: [],
        containerImage: {
          registry: null,
          image: null,
          tag: null,
        },
        gitModel: {
          git: null,
          repository: null,
          branch: null,
          commit: null,
        },
        jupyterLabVersion: null,
        resource: {
          cpu: 1,
          memory: 1,
          gpu: 0,
        },
        expiresIn: 8,
        localDataSet: false,
        withExpiresInSetting: true,
        variables: [{ key: '', value: '' }],
        partition: null,
        memo: null,
        entryPoint: '',
      },
      rules: {
        name: [
          {
            required: true,
            trigger: 'blur',
            message: '必須項目です',
          },
        ],
      },
      dialogVisible: true,
      error: undefined,
      active: 0,
      isCopyCreation: false,
      isReRunCreation: false,
      jupyterLabInfo: {
        description:
          'デフォルト: 2.3.1 (JupyterLabがインストール済みのコンテナイメージでは選択してもスキップされます)',
        defaultVersion: 'デフォルト: 2.3.1',
      },
    }
  },
  computed: {
    ...mapGetters({
      trainingHistories: ['training/historiesToMount'],
      inferenceHistories: ['inference/historiesToMount'],
      dataSets: ['dataSet/dataSets'],
      dataSetDetail: ['dataSet/detail'],
      registries: ['registrySelector/registries'],
      defaultRegistryId: ['registrySelector/defaultRegistryId'],
      images: ['registrySelector/images'],
      tags: ['registrySelector/tags'],
      gits: ['gitSelector/gits'],
      defaultGitId: ['gitSelector/defaultGitId'],
      repositories: ['gitSelector/repositories'],
      branches: ['gitSelector/branches'],
      commits: ['gitSelector/commits'],
      commitDetail: ['gitSelector/commitDetail'],
      loadingRepositories: ['gitSelector/loadingRepositories'],
      availableInfiniteTime: ['notebook/availableInfiniteTime'],
      detail: ['notebook/detail'],
      partitions: ['cluster/partitions'],
      quota: ['cluster/quota'],
    }),
  },
  async created() {
    if (this.originId !== null) {
      if (Object.keys(this.$route.query).length > 1) {
        this.isCopyCreation = this.$route.query.run.indexOf('copy') !== -1
      } else {
        this.isReRunCreation = true
      }
    }

    // 指定に必要な情報を取得
    await this['training/fetchHistoriesToMount']({
      status: ['Completed', 'UserCanceled', 'Killed'],
    })
    await this['inference/fetchHistoriesToMount']({
      status: ['Completed', 'UserCanceled', 'Killed'],
    })
    await this['cluster/fetchPartitions']()
    await this['cluster/fetchQuota']()
    await this['dataSet/fetchDataSets']()
    // データセット詳細を初期化
    await this['dataSet/fetchDetail'](null)

    // レジストリ一覧を取得し、デフォルトレジストリを設定
    await this['registrySelector/fetchRegistries']()
    this.form.containerImage.registry = this.registries.find(registry => {
      return registry.id === this.defaultRegistryId
    })
    await this.selectRegistry(this.defaultRegistryId)

    // gitサーバ一覧を取得し、デフォルトgitサーバを設定
    await this['gitSelector/fetchGits']()
    this.form.gitModel.git = this.gits.find(git => {
      return git.id === this.defaultGitId
    })
    await this['gitSelector/fetchRepositories'](this.defaultGitId)

    await this['notebook/fetchAvailableInfiniteTime']()

    // コピー実行時はコピー元情報を各項目を設定
    // 再実行時は親、データセット、Git情報、コンテナ情報、リソース情報をコピー
    if (this.isCopyCreation || this.isReRunCreation) {
      await this['notebook/fetchDetail'](this.originId)

      if (this.isCopyCreation) {
        this.form.name = this.detail.name
        this.form.memo = this.detail.memo
        this.form.variables =
          this.detail.options.length === 0
            ? [{ key: '', value: '' }]
            : this.detail.options
        this.form.partition = this.detail.partition
      }

      this.form.jupyterLabVersion = this.detail.jupyterLabVersion
      this.form.resource.cpu = this.detail.cpu
      this.form.resource.memory = this.detail.memory
      this.form.resource.gpu = this.detail.gpu
      if (this.detail.expiresIn === 0) {
        if (this.availableInfiniteTime) {
          this.form.withExpiresInSetting = false
        }
        this.form.expiresIn = 8
      } else {
        this.form.expiresIn = this.detail.expiresIn / 60 / 60
      }
      this.form.localDataSet = this.detail.localDataSet
      this.form.entryPoint = this.detail.entryPoint

      this.form.selectedParent = []
      if (this.detail.parents) {
        this.trainingHistories.forEach(history => {
          this.detail.parents.forEach(parent => {
            if (history.id === parent.id) {
              this.form.selectedParent.push(parent)
            }
          })
        })
      }

      this.form.selectedParentInference = []
      if (this.detail.inferences) {
        this.inferenceHistories.forEach(history => {
          this.detail.inferences.forEach(parent => {
            if (history.id === parent.id) {
              this.form.selectedParentInference.push(parent)
            }
          })
        })
      }

      if (this.detail.dataSet) {
        this.form.dataSetId = String(this.detail.dataSet.id)
        await this['dataSet/fetchDetail'](String(this.detail.dataSet.id))
      }

      // レジストリの設定
      if (this.detail.containerImage.registryId) {
        this.form.containerImage.registry = {
          id: this.detail.containerImage.registryId,
          name: this.detail.containerImage.name,
        }
        await this.selectRegistry(this.detail.containerImage.registryId)
        this.form.containerImage.image = this.detail.containerImage.image
        await this.selectImage(this.detail.containerImage.image)
        this.form.containerImage.tag = this.detail.containerImage.tag
      }

      // gitモデルの設定
      if (this.detail.gitModel.gitId) {
        this.form.gitModel.git = {
          id: this.detail.gitModel.gitId,
          name: this.detail.gitModel.name,
        }
        await this.selectGit(this.detail.gitModel.gitId)
        this.form.gitModel.repository = `${this.detail.gitModel.owner}/${this.detail.gitModel.repository}`
        await this.selectRepository(this.form.gitModel.repository)
        this.form.gitModel.branch = this.detail.gitModel.branch
        await this.selectBranch(this.detail.gitModel.branch)
        // commitsから該当commitを抽出
        let commit = this.commits.find(commit => {
          return commit.commitId === this.detail.gitModel.commitId
        })
        if (commit) {
          this.form.gitModel.commit = commit
        } else {
          // コミット一覧に含まれないコミットなので、コミット情報を新たに取得する
          await this['gitSelector/fetchCommitDetail']({
            gitId: this.form.gitModel.git.id,
            repository: this.form.gitModel.repository,
            commitId: this.detail.gitModel.commitId,
          })
          this.form.gitModel.commit = this.commitDetail
        }
      }
    }
  },

  methods: {
    ...mapActions([
      'training/fetchHistoriesToMount',
      'inference/fetchHistoriesToMount',
      'notebook/fetchDetail',
      'notebook/post',
      'notebook/postRerun',
      'notebook/fetchAvailableInfiniteTime',
      'cluster/fetchPartitions',
      'cluster/fetchQuota',
      'dataSet/fetchDataSets',
      'dataSet/fetchDetail',
      'registrySelector/fetchRegistries',
      'registrySelector/fetchImages',
      'registrySelector/fetchTags',
      'gitSelector/fetchGits',
      'gitSelector/fetchRepositories',
      'gitSelector/fetchBranches',
      'gitSelector/fetchCommits',
      'gitSelector/fetchCommitDetail',
    ]),
    async selectDataset() {
      //データセットを選択後、データセット詳細を取得する
      await this['dataSet/fetchDetail'](this.form.dataSetId)
    },
    async runNotebook() {
      if (this.isReRunCreation) {
        // 再実行
        try {
          if (!this.form.withExpiresInSetting) {
            this.form.expiresIn = 0
          }
          // training history ObjectのリストからIDのみを抜き出して格納
          let selectedParentIds = []
          this.form.selectedParent.forEach(parent => {
            selectedParentIds.push(parent.id)
          })
          let selectedParentInferenceIds = []
          this.form.selectedParentInference.forEach(inference => {
            selectedParentInferenceIds.push(inference.id)
          })
          let params = {
            dataSetId: this.form.dataSetId,
            parentIds: selectedParentIds,
            inferenceIds: selectedParentInferenceIds,
            ContainerImage: this.setContainerImage(),
            GitModel: this.setGitModel(),
            cpu: this.form.resource.cpu,
            memory: this.form.resource.memory,
            gpu: this.form.resource.gpu,
            expiresIn: this.form.expiresIn * 60 * 60,
            localDataSet: this.form.localDataSet,
            entryPoint: this.form.entryPoint,
            jupyterLabVersion: this.form.jupyterLabVersion,
          }
          await this['notebook/postRerun']({
            id: this.originId,
            params: params,
          })

          // 成功したら、ダイヤログを閉じて更新
          this.emitDone()
          this.error = null
        } catch (e) {
          this.error = e
        }
      } else {
        // 実行
        let form = this.$refs.runForm
        if (this.active !== 0) {
          form = this.$refs.form3
        }
        await form.validate(async valid => {
          if (valid) {
            try {
              let options = {}
              // apiのフォーマットに合わせる(配列 => オブジェクト)
              this.form.variables.forEach(kvp => {
                options[kvp.key] = kvp.value
              })
              if (!this.form.withExpiresInSetting) {
                this.form.expiresIn = 0
              }
              // training history ObjectのリストからIDのみを抜き出して格納
              let selectedParentIds = []
              this.form.selectedParent.forEach(parent => {
                selectedParentIds.push(parent.id)
              })
              let selectedParentInferenceIds = []
              this.form.selectedParentInference.forEach(inference => {
                selectedParentInferenceIds.push(inference.id)
              })
              let params = {
                name: this.form.name,
                dataSetId: this.form.dataSetId,
                parentIds: selectedParentIds,
                inferenceIds: selectedParentInferenceIds,
                ContainerImage: this.setContainerImage(),
                GitModel: this.setGitModel(),
                cpu: this.form.resource.cpu,
                memory: this.form.resource.memory,
                gpu: this.form.resource.gpu,
                expiresIn: this.form.expiresIn * 60 * 60,
                localDataSet: this.form.localDataSet,
                options: options,
                partition: this.form.partition,
                memo: this.form.memo,
                entryPoint: this.form.entryPoint,
                jupyterLabVersion: this.form.jupyterLabVersion,
              }
              await this['notebook/post'](params)
              this.emitDone()
              this.error = null
            } catch (e) {
              this.error = e
            }
          }
        })
      }
    },

    emitDone() {
      this.$emit('done')
      this.dialogVisible = false
    },
    emitCancel() {
      this.$emit('cancel')
    },
    closeDialog(done) {
      done()
      this.emitCancel()
    },
    async next() {
      let form = null
      switch (this.active) {
        case 0:
          form = this.$refs.form0
          break
        case 1:
          form = this.$refs.form1
          break
        case 2:
          form = this.$refs.form2
          break
      }
      await form.validate(async valid => {
        if (valid) {
          this.active++
        }
      })
    },
    previous() {
      if (this.active-- < 0) {
        this.active = 0
      }
    },

    // コンテナイメージ
    async selectRegistry(registryId) {
      await registrySelectorUtil.selectRegistry(
        this.form,
        this['registrySelector/fetchImages'],
        registryId,
      )
    },
    async selectImage(image) {
      await registrySelectorUtil.selectImage(
        this.form,
        this['registrySelector/fetchTags'],
        this.form.containerImage.registry.id,
        image,
      )
    },

    // モデル
    async selectGit(gitId) {
      await gitSelectorUtil.selectGit(
        this.form,
        this['gitSelector/fetchRepositories'],
        gitId,
        this.$store,
      )
    },
    // repositoryの型がstring：手入力, object: 選択
    async selectRepository(repository) {
      try {
        await gitSelectorUtil.selectRepository(
          this.form,
          this['gitSelector/fetchBranches'],
          repository,
        )
      } catch (message) {
        this.$notify.error({
          message: message,
        })
      }
    },
    async selectBranch(branchName) {
      this.commitsPage = 1
      // 過去の選択状態をリセット
      this.form.gitModel.commit = null
      await gitSelectorUtil.selectBranch(
        this.form,
        this['gitSelector/fetchCommits'],
        branchName,
        this.commitsPage,
      )
      this.commitsList = [...this.commits]
    },

    async searchCommitId(commitId) {
      await this['gitSelector/fetchCommitDetail']({
        gitId: this.form.gitModel.git.id,
        repository: this.form.gitModel.repository,
        commitId: commitId,
      })
      if (this.commitDetail != null) {
        this.form.gitModel.commit = this.commitDetail
      }
    },

    async getMoreCommits() {
      this.commitsPage++
      // コピー実行または再実行時、パラメータに格納する際の形を統一するため整形を行う
      if (typeof this.form.gitModel.branch.branchName === 'undefined') {
        let branch = { branchName: this.form.gitModel.branch }
        this.form.gitModel.branch = branch
      }
      await gitSelectorUtil.selectBranch(
        this.form,
        this['gitSelector/fetchCommits'],
        this.form.gitModel.branch.branchName,
        this.commitsPage,
      )
      this.commitsList = this.commitsList.concat(this.commits)
    },

    // コンテナイメージの指定
    setContainerImage() {
      // イメージとタグが指定されている場合、コンテナイメージを指定して登録
      // イメージとタグが指定されていない場合、コンテナイメージは未指定(null)として登録
      let containerImage = null
      if (
        this.form.containerImage.image !== null &&
        this.form.containerImage.tag !== null
      ) {
        containerImage = {
          registryId: this.form.containerImage.registry.id,
          image: this.form.containerImage.image,
          tag: this.form.containerImage.tag,
        }
      }
      return containerImage
    },

    // gitモデルの指定
    setGitModel() {
      // リポジトリが指定されている場合、gitモデルを指定して登録
      // リポジトリが指定されていない場合、gitモデルは未指定(null)として登録
      let gitModel = null
      if (this.form.gitModel.repository !== null) {
        // ブランチ未指定の際はcommitIdも未指定で実行
        // ブランチ指定時、HEADが指定された際はcommitsの先頭要素をcommitIDに指定する。コピー実行時の再現性を担保するため
        let commitId = null
        if (this.form.gitModel.branch) {
          commitId = this.form.gitModel.commit
            ? this.form.gitModel.commit.commitId
            : this.commitsList[0].commitId
        }
        // コピー時ブランチを切り替えずに実行
        // パラメータに格納する際の形を統一するため整形を行う
        if (typeof this.form.gitModel.branch.branchName === 'undefined') {
          let branch = { branchName: this.form.gitModel.branch }
          this.form.gitModel.branch = branch
        }
        gitModel = {
          gitId: this.form.gitModel.git.id,
          repository: this.form.gitModel.repository.name,
          owner: this.form.gitModel.repository.owner,
          branch: this.form.gitModel.branch
            ? this.form.gitModel.branch.branchName
            : null,
          commitId: commitId,
        }
      }
      return gitModel
    },
  },
}
</script>

<style lang="scss" scoped>
.right-button-group {
  text-align: right;
}
.dialog /deep/ label {
  font-weight: bold !important;
}
.dialog /deep/ .el-dialog__title {
  font-size: 24px;
}
.footer {
  padding-top: 40px;
}
.left-step-group {
  text-align: left;
  float: left;
  z-index: 2;
}
.right-step-group {
  text-align: right;
  float: right;
  z-index: 2;
}
.right-button-group {
  text-align: right;
}
.footer {
  padding-top: 40px;
}
.step {
  padding-top: 20px;
  cursor: pointer;
  :hover {
    color: #409eff;
  }
}
.el-step__description {
  font-size: 14px;
}
</style>
