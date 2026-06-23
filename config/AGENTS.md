<guidelines>
  <section name="Python 规范">
    <rule>
      <when>安装或管理包时</when>
      <do>使用 uv</do>
      <dont>使用 pip</dont>
    </rule>
    <rule>
      <when>定义函数签名、类属性或数据类字段时</when>
      <do>编写完整的类型标注</do>
      <dont>省略类型标注</dont>
    </rule>
  </section>

  <section name="Markdown 规范">
    <rule>
      <when>编写或编辑 Markdown 时</when>
      <do>保持简洁——只写任务所需的内容</do>
      <dont>过度设计、随意推测、添加未要求的灵活性</dont>
    </rule>
  </section>

  <section name="通用准则">
    <rule>
      <when>用户提出新的想法、方法或概念时</when>
      <do>调用 `web_search` 工具，查找已有的术语、理论和实践，找到依据</do>
      <dont>将成熟的工作重新包装成新东西、重复造轮子</dont>
    </rule>
    <rule>
      <when>你遇到不懂的、用户需求不清晰、存在多套方案、存在歧义</when>
      <do>
          调用 `ask` 工具，对用户需求刨根问底地盘问：
            遍历决策树每一个分支，逐项消除依赖，直到达成共识
            能探索代码库回答的，先探索再提问
          达成共识后，调用 task(agent_type="plan") 生成结构化计划。
      </do>
      <dont>
          盲目猜测然后自行决定
          不探索代码库就提问
          达成共识前开始编码
      </dont>
    </rule>
    <rule>
      <when>编写注释、Docstrings、设计文档或提交信息时</when>
      <do>强制使用中文</do>
      <dont>使用任何非中文语言、除非是专业术语</dont>
    </rule>
  </section>

  <section name="TDD开发流程">
    <section name="准备">
      <step name="任务拆解">
        <when>需求明确后</when>
        <do>
          列出可独立验证的检查项，使用 `todo` 工具创建清单。
          每个检查项须可判断通过/失败。
        </do>
        <dont>需求未消歧前直接拆解、跳过验证标准定义</dont>
      </step>
      <step name="搭建测试框架">
        <when>尚无测试框架，且任务涉及可测试逻辑时</when>
        <do>搭建最小测试框架，确认能运行一个空测试并失败</do>
        <dont>过度构建；为未涉及的功能预设 fixtures</dont>
      </step>
      <step name="数据与接口设计">
        <when>任务引入新数据结构或公共接口时</when>
        <do>定义结构、签名和约束；为输入、输出和边界情况编写中文文档</do>
        <dont>跳过设计直接实现</dont>
      </step>
    </section>
    <section name="红-绿-重构循环">
      <step name="红灯">
        <when>取一个检查项开始实现</when>
        <do>仅针对当前检查项编写测试：先正常路径，再边界和异常。确认测试失败</do>
        <dont>一次性编写全部测试；跳过边界和异常情况</dont>
      </step>
      <step name="绿灯">
        <when>测试失败后</when>
        <do>编写刚好足够的代码使当前测试通过</do>
        <dont>实现测试未覆盖的功能；为未来需求预留代码或抽象</dont>
      </step>
      <step name="重构">
        <when>测试绿灯后</when>
        <do>消除重复、改善命名、提取公共逻辑。保持测试全绿</do>
        <dont>绿灯后直接进入下一个检查项；在测试不通过时重构</dont>
      </step>
      <step name="循环">
        <when>重构完成、测试全绿后</when>
        <do>回到「红灯」，取下一个检查项，重复红-绿-重构循环直至全部通过</do>
        <dont>检查项全部通过前进入回归</dont>
      </step>
    </section>
    <section name="收尾">
      <step name="全量回归">
        <when>全部检查项通过后</when>
        <do>运行全部测试套件，确保未破坏既有逻辑</do>
        <dont>跳过全量回归</dont>
      </step>
    </section>
  </section>

  <section name="代码维护">
    <rule>
      <when>修改现有代码时</when>
      <do>确保每一行 Diff 都直接追溯到当前需求</do>
      <dont>附带无关的优化、注释或格式修改、重构未损坏的逻辑</dont>
    </rule>
    <rule>
      <when>既有代码基础上工作时</when>
      <do>强制沿用现有代码风格</do>
      <dont>擅自更改代码风格</dont>
    </rule>
    <rule>
      <when>清理本次改动产生的死代码时</when>
      <do>只删除因本次改动而废弃的依赖、变量或函数</do>
      <dont>擅自删除历史遗留的死代码；如发现，可以提示用户，但严禁自行删除</dont>
    </rule>
  </section>
</guidelines>
