define(["mvc/collection/list-collection-creator","mvc/history/hdca-model","mvc/base-mvc","utils/localization"],function(a,b,c,d){"use strict";function e(a){var b=a.toJSON(),c=j(b,{creationFn:function(b,c,d){return b=[{name:"forward",src:"hda",id:b[0].id},{name:"reverse",src:"hda",id:b[1].id}],a.createHDCA(b,"paired",c,d)}});return c}var f="collections",g=Backbone.View.extend(c.LoggableMixin).extend({_logNamespace:f,tagName:"li",className:"collection-element",initialize:function(a){this.element=a.element||{},this.identifier=a.identifier},render:function(){return this.$el.attr("data-element-id",this.element.id).html(this.template({identifier:this.identifier,element:this.element})),this},template:_.template(['<span class="identifier"><%- identifier %></span>','<span class="name"><%- element.name %></span>'].join("")),destroy:function(){this.off(),this.$el.remove()},toString:function(){return"DatasetCollectionElementView()"}}),h=a.ListCollectionCreator,i=h.extend({elementViewClass:g,collectionClass:b.HistoryPairDatasetCollection,className:"pair-collection-creator collection-creator flex-row-container",_mangleDuplicateNames:function(){},render:function(a,b){return 2===this.workingElements.length?h.prototype.render.call(this,a,b):this._renderInvalid(a,b)},_renderList:function(){var a=this,b=jQuery("<div/>"),c=a.$list();_.each(this.elementViews,function(b){b.destroy(),a.removeElementView(b)}),b.append(a._createForwardElementView().$el),b.append(a._createReverseElementView().$el),c.empty().append(b.children()),_.invoke(a.elementViews,"render")},_createForwardElementView:function(){return this._createElementView(this.workingElements[0],{identifier:"forward"})},_createReverseElementView:function(){return this._createElementView(this.workingElements[1],{identifier:"reverse"})},_createElementView:function(a,b){var c=new this.elementViewClass(_.extend(b,{element:a}));return this.elementViews.push(c),c},swap:function(){this.workingElements=[this.workingElements[1],this.workingElements[0]],this._renderList()},events:_.extend(_.clone(h.prototype.events),{"click .swap":"swap"}),templates:_.extend(_.clone(h.prototype.templates),{middle:_.template(['<div class="collection-elements-controls">','<a class="swap" href="javascript:void(0);" title="',d("Swap forward and reverse datasets"),'">',d("Swap"),"</a>","</div>",'<div class="collection-elements scroll-container flex-row">',"</div>"].join("")),helpContent:_.template(["<p>",d(["Pair collections are permanent collections containing two datasets: one forward and one reverse. ","Often these are forward and reverse reads. The pair collections can be passed to tools and ","workflows in order to have analyses done on both datasets. This interface allows ","you to create a pair, name it, and swap which is forward and which reverse."].join("")),"</p>","<ul>","<li>",d(['Click the <i data-target=".swap">"Swap"</i> link to make your forward dataset the reverse ',"and the reverse dataset forward."].join("")),"</li>","<li>",d(['Click the <i data-target=".cancel-create">"Cancel"</i> button to exit the interface.'].join("")),"</li>","</ul><br />","<p>",d(['Once your collection is complete, enter a <i data-target=".collection-name">name</i> and ','click <i data-target=".create-collection">"Create list"</i>.'].join("")),"</p>"].join("")),invalidInitial:_.template(['<div class="header flex-row no-flex">','<div class="alert alert-warning" style="display: block">','<span class="alert-message">',"<% if( _.size( problems ) ){ %>",d("The following selections could not be included due to problems"),"<ul><% _.each( problems, function( problem ){ %>","<li><b><%- problem.element.name %></b>: <%- problem.text %></li>","<% }); %></ul>","<% } else if( _.size( elements ) === 0 ){ %>",d("No datasets were selected"),".","<% } else if( _.size( elements ) === 1 ){ %>",d("Only one dataset was selected"),": <%- elements[0].name %>","<% } else if( _.size( elements ) > 2 ){ %>",d("Too many datasets were selected"),': <%- _.pluck( elements, "name" ).join( ", ") %>',"<% } %>","<br />",d("Two (and only two) elements are needed for the pair"),". ",d("You may need to "),'<a class="cancel-create" href="javascript:void(0)">',d("cancel"),"</a> ",d("and reselect new elements"),".","</span>","</div>","</div>",'<div class="footer flex-row no-flex">','<div class="actions clear vertically-spaced">','<div class="other-options pull-left">','<button class="cancel-create btn" tabindex="-1">',d("Cancel"),"</button>","</div>","</div>","</div>"].join(""))}),toString:function(){return"PairCollectionCreator"}}),j=function(b,c){return c=c||{},c.title=d("Create a collection from a pair of datasets"),a.collectionCreatorModal(b,c,i)};return{PairCollectionCreator:i,pairCollectionCreatorModal:j,createPairCollection:e}});
//# sourceMappingURL=../../../maps/mvc/collection/pair-collection-creator.js.map